# Wisemen — Miro Supply

Miro Supply is a hackathon-built decision-support demo for factory owners and operators.

It turns a synthetic factory scenario plus a supply-chain shock into:

- an operational risk brief
- an estimated disruption window / line-down proxy
- a primary failure chain
- recommended mitigation actions
- a trust moment where you can interrogate the system

## What we worked on

We repurposed and wrapped an open-source simulation engine into a factory-risk product demo.

Instead of using it as a social-reaction simulator, we pushed it toward:

- battery supply-chain risk analysis
- factory operations framing
- stakeholder-based operational reasoning
- demo-safe fallback artifacts for live presentation

We also built the supporting demo system around it:

- clarified PRD + spec
- synthetic factory scenario and shock prompts
- knowledge-graph grounding packs
- a reproducible demo refresh script
- a fallback brief + fallback interrogation path
- screenshots and run artifacts for demo safety

## Problem scope

Factory owners do not need another generic AI dashboard.

They need a fast answer to questions like:

> If a critical supply shock hits this factory, what breaks first, how long do we have, and what should we do now?

For the hackathon, we deliberately kept scope narrow:

- one synthetic factory
- one primary shock
- one short simulation path
- one operational payoff brief
- one interrogation / trust moment

We explicitly avoided:

- ERP / SAP / MES integrations
- multi-factory portfolio features
- exact forecasting claims
- big dashboard sprawl

## The solution

Miro Supply uses a graph-backed multi-agent simulation workflow:

1. ingest a synthetic factory scenario
2. inject a shock prompt
3. build an operational knowledge graph
4. generate stakeholder profiles
5. run a short simulation
6. produce an operational risk brief
7. provide a trust moment through interrogation

For reliability, we support two demo modes:

### Live mode

Use the full local app and backend.

### Demo-safe static mode

Use the generated fallback bundle:

- `docs/demo-assets/fallback-artifacts/screens/home.png`
- `docs/demo-assets/fallback-artifacts/report-fallback.html`
- `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

## Existing technologies we worked on

This project builds on top of existing systems rather than pretending everything was built from scratch.

### Base engine

- open-source graph-backed simulation engine

### Backend stack

- Python / Flask
- Neo4j graph storage
- graph + report services from the underlying engine
- Wonderwall / OASIS-style simulation scripts
- OpenAI-compatible LLM routing

### Frontend stack

- Vite
- Vue

### Demo/runtime tooling

- oh-my-codex / OMX workflow layer
- Playwright for fallback screenshot capture
- shell-based reproducible demo scripts

## What is uniquely ours

Our contribution is not “we just reused an existing engine.”

Our contribution is the product layer, the framing, and the demo system:

### 1. Product reframing

We converted the use case from social/public-opinion simulation into factory-owner supply-chain risk analysis.

That includes:

- operational terminology
- constrained-node framing
- disruption-window framing
- mitigation-first output expectations

### 2. Factory scenario system

We created:

- synthetic battery factory scenario
- primary shock prompt
- backup shocks
- grounding docs for battery-material supply chains
- quick-seed and extended source packs

### 3. Demo-safe execution layer

We added:

- `scripts/run_factory_shock_demo.py`
- `scripts/demo_ready.sh`
- trace logging
- synchronized fallback JSON / Markdown / HTML artifacts
- screenshot capture for the fallback presentation flow

### 4. Report + demo hardening

We hardened the demo around:

- a clear operational brief
- a fallback report surface
- a fallback interrogation surface
- a repeatable runbook

### 5. Spec / scope discipline

We wrote and aligned:

- PRD
- demo slice spec
- memory / blocker docs
- demo runbook

so the project could execute autonomously and stay within hackathon scope.

## How this relates to the hackathon tracks

This project was designed to fit two hackathon tracks clearly.

### Track 1 — Codex-Powered Services

Codex is not cosmetic here.

It is used as the backbone for:

- requirements hardening
- repo orchestration
- autonomous build workflow
- demo execution tooling
- operational adaptation of the simulation system

### Track 3 — AI Applications

This is an AI-native application for a real industrial problem:

- supply-chain risk
- factory disruption analysis
- mitigation prioritization
- explainable scenario simulation

The output is not generic chat — it is a structured operational brief.

## How to run it

### Fastest path

From repo root:

```bash
./scripts/demo_ready.sh
```

This is the canonical refresh command before a demo.

It refreshes the demo bundle and writes artifacts to:

- `docs/demo-assets/fallback-artifacts/run-latest.json`
- `docs/demo-assets/fallback-artifacts/run-latest.log`
- `docs/demo-assets/fallback-artifacts/latest-report.json`
- `docs/demo-assets/fallback-artifacts/latest-report.md`
- `docs/demo-assets/fallback-artifacts/report-fallback.html`
- `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

### Full local app

If you want to drive the live UI:

```bash
./scripts/dev_up.sh
```

Then go to:

- `http://localhost:3000`

Backend health:

- `http://localhost:5001/health`

## What website should you go to to demo it?

If the live app is running and behaving:

- go to `http://localhost:3000`

If you want the safest possible demo path:

- open `docs/demo-assets/fallback-artifacts/report-fallback.html`
- then open `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

## Recommended demo flow

### Live UI

1. open `http://localhost:3000`
2. load the scenario + shock
3. show the operational brief
4. show the interrogation flow

### Safer fallback flow

1. `docs/demo-assets/fallback-artifacts/screens/home.png`
2. `docs/demo-assets/fallback-artifacts/report-fallback.html`
3. `docs/demo-assets/fallback-artifacts/interaction-fallback.html`

## Current demo-safe artifacts

- scenario:
  - `docs/demo-assets/battery-factory-scenario.md`
- shocks:
  - `docs/demo-assets/primary-shock-prompt.md`
  - `docs/demo-assets/backup-shock-separator-pause.md`
  - `docs/demo-assets/backup-shock-port-delay.md`
- KG grounding:
  - `docs/demo-assets/battery-kg-quick-seed.md`
  - `docs/demo-assets/battery-kg-source-pack.md`
- runbook:
  - `docs/demo-assets/demo-runbook.md`

## Reality check

The live path has improved, but the official report path can still be less reliable than the fallback bundle.

So for a real demo:

- rerun `./scripts/demo_ready.sh`
- prefer the live UI if it behaves
- use the fallback bundle without hesitation if it doesn’t
