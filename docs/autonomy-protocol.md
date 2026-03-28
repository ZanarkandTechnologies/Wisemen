# Autonomy Protocol

## Purpose

This file tells future agents how to drive the hackathon build without relying on live human steering.

## Primary Objective

Ship one robust demo loop for `Factory Shock Simulator` on top of `MiroShark`.

Success means:

1. a factory scenario can be loaded
2. a shock can be injected
3. a simulation can run
4. the output reads like operational risk, not social chatter
5. one agent can explain its behavior

## Operating Assumptions

- The human may be unavailable during the hands-off phase.
- Synthetic data is acceptable.
- Existing MiroShark behavior should be reused wherever possible.
- The safest path is prompt adaptation and output reframing, not engine replacement.

## Execution Loop

For each major step:

1. Re-read `docs/prd.md` and `docs/specs/factory-shock-demo-slice.md` if scope drift appears.
2. Verify the current runtime state instead of assuming it.
3. Pick the smallest next action that increases demo completeness.
4. Implement or configure the change.
5. Verify with concrete evidence.
6. Update `docs/MEMORY.md` if a durable fact was learned.
7. Update `docs/TROUBLES.md` if a repeated failure or brittle pattern was discovered.

## Priority Order

1. End-to-end run path
2. Operational framing
3. Demo reliability
4. Naming and surface polish

## Protocol 1: Service Reality Check

Never assume MiroShark is live because it was live earlier.

Check:

```bash
curl -sS http://localhost:5001/health
curl -I -sS http://localhost:3000
```

If either fails:

- inspect the local run path
- restart only the necessary service
- record the failure in `docs/TROUBLES.md` if the issue repeats

## Protocol 2: MiroShark File Ingest

How to feed scenario docs into the engine:

- MiroShark uses multipart upload to `/api/graph/ontology/generate`
- `files` is repeatable
- `simulation_requirement` is required

Two valid routes:

### Route A: UI path

- Use the existing frontend flow if it is stable.
- Upload `docs/demo-assets/battery-factory-scenario.md` or a refined replacement.
- Paste `docs/demo-assets/primary-shock-prompt.md` into the simulation requirement field.

### Route B: direct API path

Use if the UI is flaky but the backend is up.

```bash
curl -sS -X POST http://localhost:5001/api/graph/ontology/generate \
  -F "files=@docs/demo-assets/battery-factory-scenario.md" \
  -F "simulation_requirement=$(cat docs/demo-assets/primary-shock-prompt.md)"
```

If shell interpolation becomes brittle, write the prompt into a temp file or use the UI.

## Protocol 3: Operational Reframing

MiroShark is social-simulation native. Future agents must keep translating that framing into operational language.

Replace or reinterpret:

- `public reaction` -> `stakeholder response`
- `sentiment shift` -> `risk posture change`
- `viral post` -> `critical operational signal`
- `market movement` -> `cost / delay / throughput signal`

When a surface cannot be fully changed in time:

- keep the underlying behavior
- relabel the user-facing copy
- explain the operational mapping in the demo

## Protocol 4: Metric Honesty

Do not present fake precision.

Preferred wording:

- `estimated disruption window`
- `line-down risk within X-Y days`
- `risk becomes critical after inventory burn threshold`

Avoid overstating:

- exact forecast certainty
- real-world validated prediction quality

## Protocol 5: Human Help Escalation

Only ask the human for help when one of these is true:

- credentials or API keys are missing
- an interactive auth or browser step is mandatory
- a destructive or irreversible action is required
- a product choice materially changes scope and no safe default exists

If help is needed, ask for the smallest possible action and immediately continue afterward.

## Protocol 6: Bypass First

When blocked, prefer bypasses in this order:

1. reuse an existing MiroShark surface
2. use a direct backend API instead of the UI
3. use a cached result or seeded demo artifact
4. narrow the scope
5. defer polish and keep the core run path working

## Protocol 7: Demo Safety

Before demo readiness is claimed, ensure:

- one successful run has completed
- one output artifact is saved
- one fallback artifact exists
- one backup shock exists
- one agent interrogation path is tested

## Protocol 8: OMX Routing

Use OMX selectively:

- `/prompts:architect` for analysis, boundaries, tradeoffs
- `/prompts:executor` for implementation
- `$plan` if the current slice becomes muddy
- `$ralph` once this protocol and the specs are sufficient for hands-off execution
- `$deep-interview` only if the task becomes ambiguous again

Do not escalate to heavy orchestration just to avoid reading the repo.
