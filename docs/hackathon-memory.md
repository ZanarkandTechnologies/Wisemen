# Hackathon Memory

## Event Truth

- Event: Ralphthon SF on 2026-03-28.
- Hacking starts at 10:00 AM. Autonomous agent phase starts at 12:30 PM.
- Demo format: roughly 3 minutes live plus 1-2 minutes Q&A.
- Judging favors live demo quality, originality, impact potential, and low lobster count.
- Submission must be public, new work only, and demo only hackathon-built functionality.

## Chosen Direction

- Product: `Factory Shock Simulator`.
- Base engine: `MiroShark`, already being set up in a separate task.
- Hackathon tracks to target: `Codex-Powered Services` and `AI Applications`.
- Optional stretch angle: lightweight agent-facing CLI so the project also smells agent-first without making that the core bet.

## Product Thesis

Factories do not need another generic chatbot. They need a fast way to answer:

`If this shock hits my supply chain, how many days do I have before production breaks, why, and what should I do first?`

The product uses Codex plus a MiroShark-style multi-agent simulation to turn a synthetic factory scenario plus a shock event into:

- a causal failure chain
- an estimated tipping point / days-to-disruption signal
- recommended mitigations
- agent-level explanations from simulated stakeholders

## Core Demo Shape

- Input: one synthetic factory scenario document.
- Input: one shock prompt such as export ban, port delay, or supplier failure.
- Agents: supplier, procurement, plant manager, logistics, regulator, OEM customer.
- State to reason about: inventory, lead time, cost, throughput, downtime risk.
- Output: timeline, top risks, days until line-down, mitigation actions, agent interview.

## Hard Scope Decisions

- One factory only.
- One shock only.
- One scenario document only.
- Fake data is acceptable and preferred over integration work.
- No ERP or MES integration in the MVP.
- No claim of precise forecasting accuracy; position it as a decision-support simulator.
- Reuse MiroShark primitives as much as possible instead of rewriting the engine.

## Why This Is Strong

- Real industrial pain with obvious economic stakes.
- Demoable with synthetic data.
- Uses Codex as the backbone instead of as a thin chat wrapper.
- Easy judge story: "simulate cascading operational failure, not social opinion."
- Clear before/after: chaos becomes a mitigation brief.

## Immediate Prep Before Ralph

- Prepare one crisp synthetic scenario doc for a factory with dependencies and inventories.
- Prepare 2-3 shock variants and pick one as the primary demo.
- Confirm the smallest MiroShark flow that already works locally.
- Decide the MVP output surface: report first, custom UI second.
- Prewrite the demo script and fallback narrative.

## Demo Promise

By the end of the hackathon, you should be able to say:

`We upload a factory scenario, inject a supply-chain shock, simulate the cascade, and get a live operational risk brief with mitigations and an agent we can interrogate.`
