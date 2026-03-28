# Local Agent Contract

This repository is in a hands-off hackathon mode. Operate autonomously by default.

## Startup Read Order

Before planning or editing, read these files in order:

1. `PROJECT_RULES.md`
2. `docs/autonomy-protocol.md`
3. `docs/blockers-and-bypasses.md`
4. `docs/prd.md`
5. `docs/specs/factory-shock-demo-slice.md`
6. `docs/MEMORY.md`
7. `docs/TROUBLES.md`

## Mission

Ship the smallest credible live demo for `Factory Shock Simulator` on top of `MiroShark`.

Core demo path:

- load one synthetic factory scenario
- inject one supply shock
- run one short simulation
- show one operational risk brief
- interrogate one agent

## Operating Mode

- Prefer autonomous action over questions.
- Ask the human only for secrets, external credentials, irreversible actions, or interactive steps the agent cannot perform.
- Reuse MiroShark flows and surfaces before building new ones.
- Prefer the existing report and agent interaction surfaces over a custom dashboard.
- Fake data is acceptable. Precision theater is not.

## Memory And Recovery

- Treat `docs/MEMORY.md` as the durable human-readable project memory.
- Treat `docs/TROUBLES.md` as the append-only log for repeated failures, brittle commands, and corrective lessons.
- Keep `.omx/` state updated when useful, but do not rely on it as the only source of truth.

## Build Priorities

1. Make the end-to-end scenario run work.
2. Make the output legible as operational risk, not social sentiment.
3. Make the demo robust with fallback artifacts.
4. Only then polish naming or UI.

## Verification

- Re-verify service availability before assuming MiroShark is running.
- Verify with evidence after each major step.
- If blocked, consult `docs/blockers-and-bypasses.md`, choose the cheapest bypass, and continue.

## OMX Guidance

- Use `/prompts:architect` for scoped analysis.
- Use `/prompts:executor` for focused implementation.
- Use `$plan` only if the current slice becomes unclear.
- Use `$ralph` once the PRD, spec, and blocker protocols are good enough to support hands-off execution.
- Use `$deep-interview` only if intent becomes ambiguous again.
