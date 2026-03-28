# Project Rules

## Product

- Project: `Factory Shock Simulator`
- Base engine: `MiroShark`
- Demo target: live hackathon demo in roughly 3 minutes

## Scope Rules

- One factory
- One primary shock
- One main scenario document
- One successful run path
- One report or summary payoff screen
- One working agent interrogation flow

## Non-Goals

- ERP / MES / SAP integrations
- multi-factory support
- production auth or billing
- numerically precise forecasting claims
- large custom frontend rewrites

## Important Paths

- Product planning: `docs/prd.md`
- Demo slice: `docs/specs/factory-shock-demo-slice.md`
- Demo scenario: `docs/demo-assets/battery-factory-scenario.md`
- Shock prompt: `docs/demo-assets/primary-shock-prompt.md`
- Hands-off protocol: `docs/autonomy-protocol.md`
- Blocker register: `docs/blockers-and-bypasses.md`
- Durable memory: `docs/MEMORY.md`
- Trouble log: `docs/TROUBLES.md`
- Engine repo: `MiroShark/`

## Known MiroShark Ingest Contract

MiroShark accepts multipart uploads at:

- backend route: `/api/graph/ontology/generate`

Expected form fields:

- `files`: one or more uploaded files
- `simulation_requirement`: required
- `project_name`: optional
- `additional_context`: optional

Relevant code references:

- `MiroShark/frontend/src/views/MainView.vue`
- `MiroShark/frontend/src/api/graph.js`
- `MiroShark/backend/app/api/graph.py`

## Verification Commands

Run from repo root unless noted:

```bash
curl -sS http://localhost:5001/health
curl -I -sS http://localhost:3000
```

If services are not up, switch into `MiroShark/` and use the project scripts:

```bash
npm run backend
npm run frontend
npm run dev
```

## Quality Bar

- Prefer adapting prompts, labels, and report framing over deep engine rewrites.
- Favor short, testable changes.
- Preserve demo reliability over technical ambition.
