# Durable Memory

## Product

- We are building `Factory Shock Simulator`.
- It is a hackathon demo built on top of `MiroShark`.
- The intended tracks are `Codex-Powered Services` and `AI Applications`.

## Demo Thesis

- Simulate causal operational failure chains, not public opinion.
- Input: one synthetic factory scenario and one shock event.
- Output: one operational risk brief plus one agent explanation.
- Product posture: supply-chain risk decision tool for factory owners, not a dashboard.

## Current Demo Assets

- Scenario doc: `docs/demo-assets/battery-factory-scenario.md`
- Shock prompt: `docs/demo-assets/primary-shock-prompt.md`
- Backup shock prompt: `docs/demo-assets/backup-shock-separator-pause.md`
- Backup shock prompt: `docs/demo-assets/backup-shock-port-delay.md`
- Fallback artifact staging: `docs/demo-assets/fallback-artifacts/`

## Planning Artifacts

- PRD: `docs/prd.md`
- Spec: `docs/specs/factory-shock-demo-slice.md`
- OMX PRD artifact: `.omx/plans/prd-factory-shock-simulator.md`
- OMX test spec artifact: `.omx/plans/test-spec-factory-shock-simulator.md`
- Deep interview source of truth: `.omx/specs/deep-interview-factory-shock-spec-direction.md`
- Ralph execution brief: `.omx/specs/ralph-execution-brief-factory-shock.md`

## Critical Scope Guardrails

- one scenario
- one shock
- one working run path
- one payoff screen
- one agent interrogation
- no dashboard sprawl
- no generic factory copilot
- no enterprise integrations
- no fake precision claims

## Review Loop

- Run one primary shock and keep backup shocks ready.
- After meaningful changes, use a separate verifier/test-oriented agent to validate the workflow.
- Save fallback evidence: cached run, saved report, or screenshots.

## Trust Recipe

- show the causal failure chain
- show the constrained node / tipping point
- show one grounded agent explanation tied to the same shock
- show mitigation actions linked back to that chain

## MiroShark Ingest Fact

The engine accepts multipart uploads at `/api/graph/ontology/generate` with repeatable `files` parts and a required `simulation_requirement` field.

## Hands-Off Rule

Future agents should read `docs/autonomy-protocol.md` and `docs/blockers-and-bypasses.md` before implementation work.

- Verification rule: do not self-certify implementation; delegate verification/testing to a separate verifier-oriented agent whenever possible.
- Demo safety rule: live path preferred, but fallback artifacts are valid when runtime is brittle.
