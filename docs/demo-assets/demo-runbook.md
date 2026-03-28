# Miro Supply Demo Runbook

Last updated: March 28, 2026

## Goal

Show a factory owner-style workflow:

1. load one synthetic battery-factory scenario
2. inject one supply-chain shock
3. run a short simulation
4. show one operational risk brief
5. interrogate one agent / analyst about the result

## Recommended live setup

- Backend: `http://localhost:5001`
- Frontend: `http://localhost:3000`
- Primary scenario: `docs/demo-assets/battery-factory-scenario.md`
- Canonical grounding file for the scripted run: `docs/demo-assets/battery-kg-quick-seed.md`
- Extended research pack for future graph enrichment: `docs/demo-assets/battery-kg-source-pack.md`
- Primary shock: `docs/demo-assets/primary-shock-prompt.md`
- Backup shocks:
  - `docs/demo-assets/backup-shock-separator-pause.md`
  - `docs/demo-assets/backup-shock-port-delay.md`

## Two operating modes

### Live mode

Use the local backend/frontend if you want to show the full application flow.

### Demo-safe static mode

After running `./scripts/demo_ready.sh`, you can present the fallback bundle without relying on the live frontend routes:

- `docs/demo-assets/fallback-artifacts/screens/home.png`
- `docs/demo-assets/fallback-artifacts/report-fallback.html`
- `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

If the local services are down at demo time, use the most recently refreshed static bundle as-is.

## Enterprise-style demo posture

Say this like an operational decision tool, not an AI toy:

- `operational risk brief`, not `prediction report`
- `estimated disruption window / line-down proxy`, not exact forecast certainty
- `stakeholders`, not personas
- `constrained node`, `failure chain`, `mitigation actions`

## Fastest functional run path

From repo root:

```bash
./scripts/demo_ready.sh
```

This is the canonical refresh command. Run it again right before the live demo to refresh IDs and fallback artifacts.

What it does:

1. health-checks the backend
2. uploads the scenario + shock
3. uploads the knowledge-graph source pack for extra supplier/material grounding
4. generates ontology
5. builds the graph
6. creates the simulation
7. prepares profiles/config
8. runs a short simulation
9. generates the report
10. saves fallback artifacts locally

## Canonical demo-safe payoff asset

If the live report path feels slow or brittle, use this as the clean enterprise-looking payoff surface:

- `docs/demo-assets/fallback-artifacts/report-fallback.html`

This file now includes an embedded trust-moment interrogation snippet, so it can stand alone if needed.

Screenshot companion:

- `docs/demo-assets/fallback-artifacts/screens/report-fallback.png`

## Canonical trust-moment fallback asset

If the live interaction surface feels slow or brittle, use this:

- `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

Screenshot companion:

- `docs/demo-assets/fallback-artifacts/screens/interaction-fallback.png`

## Canonical opening fallback asset

If you need a static opening frame before showing the payoff:

- `docs/demo-assets/fallback-artifacts/screens/home.png`

## Debug / tracing loop

Tail these while debugging:

```bash
tail -f docs/demo-assets/fallback-artifacts/run-latest.log
cat docs/demo-assets/fallback-artifacts/run-latest.json
./scripts/tail_demo_logs.sh
```

Primary artifact outputs:

- `docs/demo-assets/fallback-artifacts/run-latest.log`
- `docs/demo-assets/fallback-artifacts/run-latest.json`
- `docs/demo-assets/fallback-artifacts/latest-report.json`
- `docs/demo-assets/fallback-artifacts/latest-report.md`
- `docs/demo-assets/fallback-artifacts/notes.md`

## Live demo script

### Opening

`We loaded a synthetic battery-components factory and injected a supply shock: lithium precursor exports tighten and lead times jump.`

### Simulation moment

`Instead of relying on a dashboard or a black-box forecast, the system simulates how procurement, suppliers, logistics, and the plant react across the same operating network.`

### Payoff

`Now we get an operational risk brief: what breaks first, where the constrained node is, the estimated disruption window, and what actions buy time.`

### Trust moment

`We can interrogate the analyst or one stakeholder and ask why the risk escalated. The answer should tie back to the same shock and failure chain shown in the brief.`

## Fallback plan if live runtime gets brittle

Use these in order:

1. `report-fallback.html`
2. `interaction-fallback.html`
3. saved report markdown/json from `docs/demo-assets/fallback-artifacts/`
4. screenshot set under `docs/demo-assets/fallback-artifacts/screens/`
5. backup shock file with the same product story

## What to capture before final demo

- one successful run trace json
- one saved report json
- one saved report markdown
- one screenshot of the payoff brief
- one screenshot of the interrogation surface
- one backup shock ready to paste

## If the run breaks

1. verify services:
   ```bash
   curl -sS http://localhost:5001/health
   curl -I -sS http://localhost:3000
   ```
2. restart stack:
   ```bash
   ./scripts/dev_up.sh
   ```
3. rerun the scripted demo path
4. inspect the trace log and backend log before changing code
