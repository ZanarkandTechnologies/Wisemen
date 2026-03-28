#!/usr/bin/env python3
import json
import os
import time
import subprocess
from datetime import datetime, UTC
from pathlib import Path
from html import escape

ROOT = Path(__file__).resolve().parents[1]
BACKEND = os.environ.get('FACTORY_SHOCK_BACKEND', 'http://localhost:5001')
SCENARIO = Path(os.environ.get('FACTORY_SHOCK_SCENARIO', ROOT / 'docs/demo-assets/battery-factory-scenario.md'))
SHOCK = Path(os.environ.get('FACTORY_SHOCK_SHOCK', ROOT / 'docs/demo-assets/primary-shock-prompt.md'))
KG_SOURCE_PACK = Path(os.environ.get('FACTORY_SHOCK_KG_SOURCE_PACK', ROOT / 'docs/demo-assets/battery-kg-quick-seed.md'))
MAX_ROUNDS = int(os.environ.get('FACTORY_SHOCK_MAX_ROUNDS', '2'))
USE_LLM_PROFILES = os.environ.get('FACTORY_SHOCK_USE_LLM_PROFILES', 'false').lower() == 'true'
PROFILE_PARALLELISM = int(os.environ.get('FACTORY_SHOCK_PROFILE_PARALLELISM', '8'))
PROJECT_ID_OVERRIDE = os.environ.get('FACTORY_SHOCK_PROJECT_ID', '').strip()
SIMULATION_ID_OVERRIDE = os.environ.get('FACTORY_SHOCK_SIMULATION_ID', '').strip()
ENTITY_TYPES = [x.strip() for x in os.environ.get('FACTORY_SHOCK_ENTITY_TYPES', 'Factory,Supplier,Regulator,LogisticsNode').split(',') if x.strip()]
REPORT_TIMEOUT = int(os.environ.get('FACTORY_SHOCK_REPORT_TIMEOUT', '45'))
TRACE_DIR = ROOT / 'docs/demo-assets/fallback-artifacts'
TRACE_DIR.mkdir(parents=True, exist_ok=True)
TRACE_LOG = TRACE_DIR / 'run-latest.log'
TRACE_JSON = TRACE_DIR / 'run-latest.json'
LATEST_REPORT_JSON = TRACE_DIR / 'latest-report.json'
LATEST_REPORT_MD = TRACE_DIR / 'latest-report.md'
LATEST_REPORT_HTML = TRACE_DIR / 'report-fallback.html'
INTERACTION_FALLBACK_HTML = TRACE_DIR / 'interaction-fallback.html'
NOTES_MD = TRACE_DIR / 'notes.md'
SCREEN_DIR = TRACE_DIR / 'screens'
SCREEN_DIR.mkdir(parents=True, exist_ok=True)
REPORT_SCREENSHOT = SCREEN_DIR / 'report-fallback.png'
INTERACTION_SCREENSHOT = SCREEN_DIR / 'interaction-fallback.png'

def now_iso():
    return datetime.now(UTC).isoformat().replace('+00:00', 'Z')


trace = {
    'started_at': now_iso(),
    'backend': BACKEND,
    'scenario': str(SCENARIO.relative_to(ROOT)),
    'shock': str(SHOCK.relative_to(ROOT)),
    'kg_source_pack': str(KG_SOURCE_PACK.relative_to(ROOT)),
    'max_rounds': MAX_ROUNDS,
    'use_llm_profiles': USE_LLM_PROFILES,
    'profile_parallelism': PROFILE_PARALLELISM,
    'project_id_override': PROJECT_ID_OVERRIDE or None,
    'simulation_id_override': SIMULATION_ID_OVERRIDE or None,
    'entity_types': ENTITY_TYPES,
    'report_timeout': REPORT_TIMEOUT,
    'steps': []
}


def log(msg: str):
    line = f"[{now_iso()}] {msg}"
    print(line)
    with TRACE_LOG.open('a', encoding='utf-8') as f:
        f.write(line + '\n')


def save_trace():
    TRACE_JSON.write_text(json.dumps(trace, indent=2), encoding='utf-8')


def run_curl(args, step_name, allow_failure=False):
    cmd = ['curl', '-sS', '-w', '\n%{http_code}'] + args
    log(f"RUN {step_name}: {' '.join(cmd[:-1])}")
    result = subprocess.run(cmd, capture_output=True, text=True)
    stdout = result.stdout or ''
    stderr = result.stderr or ''
    if '\n' in stdout:
        body, status_code = stdout.rsplit('\n', 1)
    else:
        body, status_code = stdout, '000'
    entry = {
        'step': step_name,
        'status_code': int(status_code) if status_code.isdigit() else status_code,
        'stderr': stderr.strip(),
    }
    try:
        entry['body'] = json.loads(body) if body.strip() else None
    except json.JSONDecodeError:
        entry['body'] = body
    trace['steps'].append(entry)
    save_trace()
    if result.returncode != 0 and not allow_failure:
        raise RuntimeError(f"curl failed for {step_name}: {stderr.strip() or result.returncode}")
    if (not allow_failure) and (not status_code.startswith('2')):
        raise RuntimeError(f"HTTP {status_code} for {step_name}: {body[:500]}")
    return entry['body']


def post_json(path, payload, step_name, allow_failure=False):
    return run_curl([
        '-X', 'POST', f"{BACKEND}{path}",
        '-H', 'Content-Type: application/json',
        '-d', json.dumps(payload),
    ], step_name, allow_failure=allow_failure)


def get_json(path, step_name, allow_failure=False):
    return run_curl([f"{BACKEND}{path}"], step_name, allow_failure=allow_failure)


def post_form_ontology(project_name='Factory Shock Demo Run'):
    args = [
        '-X', 'POST', f"{BACKEND}/api/graph/ontology/generate",
        '-F', f"files=@{SCENARIO}",
    ]
    if KG_SOURCE_PACK.exists():
        args += ['-F', f"files=@{KG_SOURCE_PACK}"]
    args += [
        '-F', f"simulation_requirement={SHOCK.read_text(encoding='utf-8')}",
        '-F', f"project_name={project_name}",
        '-F', 'additional_context=Factory-owner supply-chain risk scenario for hackathon demo',
    ]
    return run_curl(args, 'ontology.generate')


def poll_graph_task(task_id, timeout=600):
    start = time.time()
    while time.time() - start < timeout:
        data = get_json(f"/api/graph/task/{task_id}", 'graph.task.poll')
        task = data.get('data', {})
        status = str(task.get('status', '')).lower()
        log(f"Graph task status={status} progress={task.get('progress')}")
        if status == 'completed':
            return task
        if status == 'failed':
            raise RuntimeError(f"Graph build failed: {task}")
        time.sleep(2)
    raise TimeoutError('Graph build timed out')


def poll_prepare(simulation_id, task_id=None, timeout=1200):
    start = time.time()
    while time.time() - start < timeout:
        payload = {'simulation_id': simulation_id}
        if task_id:
            payload['task_id'] = task_id
        data = post_json('/api/simulation/prepare/status', payload, 'simulation.prepare.status')
        info = data.get('data', {})
        status = str(info.get('status', '')).lower()
        log(f"Prepare status={status} progress={info.get('progress')}")
        if status in ('ready', 'completed') or info.get('already_prepared'):
            return info
        if status == 'failed':
            raise RuntimeError(f"Prepare failed: {info}")
        time.sleep(3)
    raise TimeoutError('Simulation prepare timed out')


def poll_run(simulation_id, timeout=1800):
    start = time.time()
    while time.time() - start < timeout:
        data = get_json(f"/api/simulation/{simulation_id}/run-status", 'simulation.run_status')
        info = data.get('data', {})
        runner_status = str(info.get('runner_status', '')).lower()
        log(f"Run status={runner_status} rounds={info.get('twitter_current_round')}/{info.get('total_rounds')}")
        if runner_status in ('completed', 'stopped'):
            return info
        if runner_status == 'failed':
            raise RuntimeError(f"Run failed: {info}")
        time.sleep(5)
    raise TimeoutError('Simulation run timed out')


def poll_report(simulation_id, task_id=None, timeout=1800):
    start = time.time()
    while time.time() - start < timeout:
        payload = {'simulation_id': simulation_id}
        if task_id:
            payload['task_id'] = task_id
        data = post_json('/api/report/generate/status', payload, 'report.generate.status')
        info = data.get('data', {})
        status = str(info.get('status', '')).lower()
        log(f"Report status={status} progress={info.get('progress')}")
        if status == 'completed':
            return info
        if status == 'failed':
            raise RuntimeError(f"Report failed: {info}")
        time.sleep(4)
    raise TimeoutError('Report generation timed out')


def build_fallback_report(project_id, simulation_id, report_id=None):
    project = get_json(f'/api/graph/project/{project_id}', 'graph.project.for_fallback')
    proj = project.get('data', {})
    graph_id = proj.get('graph_id')
    entities_resp = get_json(f'/api/simulation/entities/{graph_id}', 'simulation.entities.for_fallback')
    entities = entities_resp.get('data', {}).get('entities', [])

    counts = {}
    for ent in entities:
        label = (ent.get('labels') or ['Unknown'])[0]
        counts[label] = counts.get(label, 0) + 1

    factories = [e['name'] for e in entities if (e.get('labels') or [''])[0] == 'Factory']
    suppliers = [e['name'] for e in entities if (e.get('labels') or [''])[0] in ('Supplier', 'Processor', 'SeparatorSupplier')]
    regulators = [e['name'] for e in entities if (e.get('labels') or [''])[0] == 'Regulator']
    logistics = [e['name'] for e in entities if (e.get('labels') or [''])[0] == 'LogisticsNode']
    customers = [e['name'] for e in entities if (e.get('labels') or [''])[0] == 'OEMCustomer']

    def prefer(candidates, preferred_names, default):
        for name in preferred_names:
            for candidate in candidates:
                if candidate.lower() == name.lower():
                    return candidate
        return candidates[0] if candidates else default

    factory = prefer(
        factories,
        ['Northstar Battery Components', 'Panasonic Energy', 'LG Energy Solution'],
        'Northstar Battery Components'
    )
    supplier = prefer(
        suppliers,
        ['Jade Ridge Lithium Materials', 'Ganfeng Lithium', 'Albemarle', 'SQM', 'Blue Mesa Lithium Chemicals'],
        'lithium precursor supplier'
    )
    regulator = regulators[0] if regulators else 'trade regulator'
    logistics_node = logistics[0] if logistics else 'logistics node'
    customer = prefer(customers, ['FleetMotion OEM', 'Ford Motor Company'], 'OEM customer')

    brief = {
        'report_id': report_id or f'fallback_{simulation_id}',
        'simulation_id': simulation_id,
        'type': 'fallback_operational_risk_brief',
        'graph_id': graph_id,
        'graph_node_count': len(entities),
        'entity_distribution': counts,
        'title': 'Operational Risk Brief — Fallback Artifact',
        'summary': proj.get('analysis_summary') or 'Fallback operational brief generated from graph/project state.',
        'primary_failure_chain': [
            'Chinese lithium precursor export restriction tightens outbound volumes',
            f'{supplier} and related upstream processors face lead-time and availability stress',
            f'{factory} burns inventory while second-tier supply buffers shrink',
            f'{logistics_node} and rerouting constraints amplify delay and cost pressure',
            f'{customer} delivery risk rises as line-down exposure increases'
        ],
        'most_constrained_node': 'Lithium precursor supply and second-tier processing capacity',
        'estimated_disruption_window': '14-21 days under current inventory assumptions',
        'recommended_actions': [
            'Expedite inbound critical precursor and separator material for the highest-risk production line',
            'Pool and reallocate inventory across customers or plants to protect near-term delivery commitments',
            'Open contingency procurement with alternate precursor or cathode processors immediately',
            'Negotiate temporary delivery flexibility with the highest-risk OEM customer',
            'Track regulator and logistics chokepoints daily and pre-book rerouting capacity'
        ],
        'confidence_note': 'Heuristic fallback artifact generated from graph state and scenario assumptions; use as demo-safe backup, not as a precise forecast.'
    }

    md = "\n".join([
        '# Operational Risk Brief — Fallback Artifact',
        '',
        f"**Factory:** {factory}",
        f"**Shock:** {SHOCK.read_text(encoding='utf-8').splitlines()[3] if len(SHOCK.read_text(encoding='utf-8').splitlines()) > 3 else 'Primary shock prompt'}",
        f"**Estimated disruption window:** {brief['estimated_disruption_window']}",
        f"**Most constrained node:** {brief['most_constrained_node']}",
        '',
        '## Primary failure chain',
        *[f'- {item}' for item in brief['primary_failure_chain']],
        '',
        '## Recommended actions',
        *[f'- {item}' for item in brief['recommended_actions']],
        '',
        f"**Confidence note:** {brief['confidence_note']}",
    ])

    LATEST_REPORT_JSON.write_text(json.dumps(brief, indent=2), encoding='utf-8')
    LATEST_REPORT_MD.write_text(md, encoding='utf-8')
    return brief


def write_report_html(report_data):
    if report_data.get('type') != 'fallback_operational_risk_brief':
        return None

    q1 = "Why does this shock become critical so fast?"
    a1 = (
        f"The factory depends on lithium precursor flow from {report_data['primary_failure_chain'][1].split(' and ')[0]}. "
        f"Once lead times stretch and replacement flow slows, {report_data['primary_failure_chain'][2]}."
    )

    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{escape(report_data.get('title', 'Operational Risk Brief'))}</title>
  <style>
    body {{ margin:0; background:#0b1020; color:#e6eef8; font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif; }}
    .wrap {{ max-width: 980px; margin: 0 auto; padding: 48px 32px 80px; }}
    .tag {{ display:inline-block; padding:6px 10px; border:1px solid rgba(148,163,184,.35); border-radius:999px; font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:#93c5fd; background:rgba(59,130,246,.08); }}
    h1 {{ font-size: 40px; line-height:1.05; margin: 18px 0 12px; }}
    .sub {{ color:#94a3b8; font-size:18px; line-height:1.6; max-width:860px; }}
    .grid {{ display:grid; grid-template-columns: repeat(2, minmax(0,1fr)); gap:16px; margin:32px 0; }}
    .card {{ background:linear-gradient(180deg, rgba(15,23,42,.95), rgba(15,23,42,.88)); border:1px solid rgba(148,163,184,.18); border-radius:20px; padding:20px; box-shadow: 0 24px 80px rgba(0,0,0,.28); }}
    .label {{ font-size:12px; text-transform:uppercase; letter-spacing:.08em; color:#94a3b8; margin-bottom:8px; }}
    .value {{ font-size:24px; font-weight:700; }}
    h2 {{ margin:34px 0 14px; font-size:22px; }}
    ul {{ margin:0; padding-left:18px; color:#dbeafe; line-height:1.7; }}
    li {{ margin: 8px 0; }}
    .foot {{ margin-top:28px; color:#94a3b8; font-size:14px; }}
    .qa {{ background:linear-gradient(180deg, rgba(15,23,42,.95), rgba(15,23,42,.88)); border:1px solid rgba(148,163,184,.18); border-radius:20px; padding:20px; margin:20px 0; }}
    .q {{ color:#93c5fd; font-size:12px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:8px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="tag">Factory Shock Simulator</div>
    <h1>{escape(report_data.get('title', 'Operational Risk Brief'))}</h1>
    <p class="sub">{escape(report_data.get('summary', ''))}</p>
    <div class="grid">
      <div class="card"><div class="label">Estimated disruption window</div><div class="value">{escape(report_data.get('estimated_disruption_window', 'n/a'))}</div></div>
      <div class="card"><div class="label">Most constrained node</div><div class="value">{escape(report_data.get('most_constrained_node', 'n/a'))}</div></div>
    </div>
    <h2>Primary failure chain</h2>
    <div class="card"><ul>{''.join(f'<li>{escape(item)}</li>' for item in report_data.get('primary_failure_chain', []))}</ul></div>
    <h2>Recommended actions</h2>
    <div class="card"><ul>{''.join(f'<li>{escape(item)}</li>' for item in report_data.get('recommended_actions', []))}</ul></div>
    <h2>Trust moment — operator interrogation</h2>
    <div class="qa">
      <div class="q">Question</div>
      <p>{escape(q1)}</p>
      <div class="q">Answer</div>
      <p>{escape(a1)}</p>
    </div>
    <p class="foot">{escape(report_data.get('confidence_note', ''))}</p>
  </div>
</body>
</html>"""
    LATEST_REPORT_HTML.write_text(html, encoding='utf-8')
    return LATEST_REPORT_HTML


def write_interaction_fallback_html(report_data):
    q1 = "Why does this shock become critical so fast?"
    a1 = (
        f"The factory depends on lithium precursor flow from {report_data['primary_failure_chain'][1].split(' and ')[0]}. "
        f"Once lead times stretch and replacement flow slows, {report_data['primary_failure_chain'][2]}."
    )
    q2 = "What would you do first as the operator?"
    a2 = report_data['recommended_actions'][0]
    html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Agent Interrogation Fallback</title>
  <style>
    body {{ margin:0; background:#0b1020; color:#e6eef8; font-family: Inter, ui-sans-serif, system-ui, -apple-system, sans-serif; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; padding: 40px 32px 80px; }}
    .tag {{ display:inline-block; padding:6px 10px; border:1px solid rgba(148,163,184,.35); border-radius:999px; font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:#93c5fd; background:rgba(59,130,246,.08); }}
    h1 {{ font-size: 36px; margin: 18px 0 12px; }}
    p {{ color:#cbd5e1; line-height:1.7; }}
    .btn {{ display:inline-flex; margin: 18px 0 24px; padding:12px 16px; border-radius:14px; text-decoration:none; font-weight:600; background:#2563eb; color:white; }}
    .qa {{ background:linear-gradient(180deg, rgba(15,23,42,.95), rgba(15,23,42,.88)); border:1px solid rgba(148,163,184,.18); border-radius:20px; padding:20px; margin:20px 0; }}
    .q {{ color:#93c5fd; font-size:12px; text-transform:uppercase; letter-spacing:.08em; margin-bottom:8px; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="tag">Factory Shock Simulator</div>
    <h1>Agent Interrogation Fallback</h1>
    <p>Use this as the trust moment if the live interaction surface is slow. It turns the same risk brief into a concise operator-style interrogation moment without depending on the live app.</p>
    <div class="qa">
      <div class="q">Question</div>
      <p>{escape(q1)}</p>
      <div class="q">Answer</div>
      <p>{escape(a1)}</p>
    </div>
    <div class="qa">
      <div class="q">Question</div>
      <p>{escape(q2)}</p>
      <div class="q">Answer</div>
      <p>{escape(a2)}</p>
    </div>
  </div>
</body>
</html>"""
    INTERACTION_FALLBACK_HTML.write_text(html, encoding='utf-8')
    return INTERACTION_FALLBACK_HTML


def try_capture_report_screenshot():
    if not LATEST_REPORT_HTML.exists():
        return None
    try:
        subprocess.run(
            [
                'npx', 'playwright', 'screenshot',
                LATEST_REPORT_HTML.resolve().as_uri(),
                str(REPORT_SCREENSHOT)
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return REPORT_SCREENSHOT
    except Exception as exc:
        log(f'Playwright screenshot skipped: {exc}')
        return None


def try_capture_interaction_screenshot():
    if not INTERACTION_FALLBACK_HTML.exists():
        return None
    try:
        subprocess.run(
            [
                'npx', 'playwright', 'screenshot',
                INTERACTION_FALLBACK_HTML.resolve().as_uri(),
                str(INTERACTION_SCREENSHOT)
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        return INTERACTION_SCREENSHOT
    except Exception as exc:
        log(f'Playwright interaction screenshot skipped: {exc}')
        return None


def main():
    TRACE_LOG.write_text('', encoding='utf-8')
    save_trace()
    log('Starting factory shock demo run')

    health = get_json('/health', 'health.check')
    if health.get('status') != 'ok':
        raise RuntimeError(f"Backend health not ok: {health}")

    if PROJECT_ID_OVERRIDE:
        project = get_json(f'/api/graph/project/{PROJECT_ID_OVERRIDE}', 'graph.project.get')
        project_id = project['data']['project_id']
        graph_id = project['data'].get('graph_id')
        if not graph_id:
            build = post_json('/api/graph/build', {'project_id': project_id, 'graph_name': 'Factory Shock Demo Graph'}, 'graph.build')
            build_task_id = build['data']['task_id']
            graph_task = poll_graph_task(build_task_id)
            graph_id = graph_task.get('result', {}).get('graph_id')
        log(f"Reusing project {project_id} with graph {graph_id}")
    else:
        ontology = post_form_ontology()
        project_id = ontology['data']['project_id']
        log(f"Created project {project_id}")

        build = post_json('/api/graph/build', {'project_id': project_id, 'graph_name': 'Factory Shock Demo Graph'}, 'graph.build')
        build_task_id = build['data']['task_id']
        graph_task = poll_graph_task(build_task_id)
        graph_id = graph_task.get('result', {}).get('graph_id')
        log(f"Built graph {graph_id}")

    if SIMULATION_ID_OVERRIDE:
        simulation_id = SIMULATION_ID_OVERRIDE
        log(f"Reusing simulation {simulation_id}")
    else:
        create = post_json('/api/simulation/create', {
            'project_id': project_id,
            'graph_id': graph_id,
            'enable_twitter': True,
            'enable_reddit': True,
            'enable_polymarket': True,
        }, 'simulation.create')
        simulation_id = create['data']['simulation_id']
        log(f"Created simulation {simulation_id}")

    prepare = post_json('/api/simulation/prepare', {
        'simulation_id': simulation_id,
        'use_llm_for_profiles': USE_LLM_PROFILES,
        'parallel_profile_count': PROFILE_PARALLELISM,
        'entity_types': ENTITY_TYPES,
    }, 'simulation.prepare')
    prepare_task_id = prepare['data'].get('task_id')
    prepare_info = poll_prepare(simulation_id, prepare_task_id)
    log('Simulation preparation complete')

    start_run = post_json('/api/simulation/start', {
        'simulation_id': simulation_id,
        'platform': 'parallel',
        'max_rounds': MAX_ROUNDS,
        'enable_graph_memory_update': True,
        'enable_cross_platform': True,
    }, 'simulation.start')
    log(f"Started simulation run: {start_run.get('data', {})}")
    run_info = poll_run(simulation_id)

    report_start = post_json('/api/report/generate', {
        'simulation_id': simulation_id,
        'force_regenerate': False,
    }, 'report.generate')
    report_task_id = report_start['data'].get('task_id')
    report_id = report_start['data'].get('report_id')
    report_data = {}
    report_fell_back = False
    try:
        report_info = poll_report(simulation_id, report_task_id, timeout=REPORT_TIMEOUT)
        report_id = report_info.get('report_id') or report_id
        if not report_id:
            raise RuntimeError(f'No report_id found: {report_info}')
        report = get_json(f'/api/report/{report_id}', 'report.get')
        report_data = report.get('data', {})
    except Exception as exc:
        log(f'Report generation fallback triggered: {exc}')
        report_fell_back = True

    report_data = build_fallback_report(project_id, simulation_id, report_id=report_id)
    markdown = LATEST_REPORT_MD.read_text(encoding='utf-8') if LATEST_REPORT_MD.exists() else ''

    interaction_html_path = write_interaction_fallback_html(report_data)
    html_path = write_report_html(report_data)
    report_screenshot_path = try_capture_report_screenshot() if html_path else None
    interaction_screenshot_path = try_capture_interaction_screenshot() if interaction_html_path else None

    summary = {
        'completed_at': now_iso(),
        'project_id': project_id,
        'graph_id': graph_id,
        'simulation_id': simulation_id,
        'report_id': report_id,
        'shock_file': str(SHOCK.relative_to(ROOT)),
        'scenario_file': str(SCENARIO.relative_to(ROOT)),
        'max_rounds': MAX_ROUNDS,
        'prepare_status': prepare_info,
        'run_status': run_info,
        'report_title': report_data.get('outline', {}).get('title') if isinstance(report_data.get('outline'), dict) else report_data.get('title'),
        'fallback_report_json': str(LATEST_REPORT_JSON.relative_to(ROOT)),
        'fallback_report_md': str(LATEST_REPORT_MD.relative_to(ROOT)) if markdown else None,
        'fallback_report_html': str(LATEST_REPORT_HTML.relative_to(ROOT)) if html_path else None,
        'fallback_interaction_html': str(INTERACTION_FALLBACK_HTML.relative_to(ROOT)) if interaction_html_path else None,
        'fallback_report_screenshot': str(report_screenshot_path.relative_to(ROOT)) if report_screenshot_path else None,
        'fallback_interaction_screenshot': str(interaction_screenshot_path.relative_to(ROOT)) if interaction_screenshot_path else None,
        'status_note': (
            'Official report timed out; deterministic fallback brief emitted from graph state and scenario assumptions.'
            if report_fell_back else
            'Official report path ran, and fallback artifacts were refreshed from graph state for demo safety.'
        ),
    }
    trace['summary'] = summary
    save_trace()

    NOTES_MD.write_text(
        '\n'.join([
            '# Demo Run Notes',
            '',
            f'- Captured: {summary["completed_at"]}',
            f'- Scenario: {summary["scenario_file"]}',
            f'- Shock: {summary["shock_file"]}',
            f'- Project ID: {project_id}',
            f'- Graph ID: {graph_id}',
            f'- Simulation ID: {simulation_id}',
            f'- Report ID: {report_id}',
            f'- Max rounds: {MAX_ROUNDS}',
            f'- Report JSON: {summary["fallback_report_json"]}',
            f'- Report Markdown: {summary["fallback_report_md"]}',
            f'- Report HTML: {summary["fallback_report_html"]}',
            f'- Interaction HTML: {summary["fallback_interaction_html"]}',
            f'- Report screenshot: {summary["fallback_report_screenshot"]}',
            f'- Interaction screenshot: {summary["fallback_interaction_screenshot"]}',
            f'- Status: {summary["status_note"]}',
            f'- Trace log: {TRACE_LOG.relative_to(ROOT)}',
            f'- Trace json: {TRACE_JSON.relative_to(ROOT)}',
        ]),
        encoding='utf-8'
    )

    print(json.dumps(summary, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as exc:
        log(f'FAILED: {exc}')
        trace['failed_at'] = now_iso()
        trace['error'] = str(exc)
        save_trace()
        raise
