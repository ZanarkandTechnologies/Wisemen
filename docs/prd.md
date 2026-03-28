# PRD: Factory Shock Simulator

## Summary

Factory Shock Simulator is a Codex-powered decision-support tool for manufacturing operators and industrial AI sellers. A user uploads a synthetic factory scenario and injects a shock event. The system runs a multi-agent cascade simulation and produces an explainable risk brief: what breaks first, how quickly disruption propagates, and which mitigation actions buy the most time.

The hackathon version is intentionally narrow. It proves the product thesis with one scenario, one shock, and one compelling live demo loop.

## Audience

### Primary user

- Factory owner / plant operator responsible for supply continuity
- Plant operations leader
- Supply chain / procurement lead
- Industrial solutions engineer selling AI into factories

### Demo audience

- Hackathon judges
- Technical builders who can quickly understand agentic simulation
- Potential future factory buyers or advisors

## Jobs To Be Done

1. When a disruptive event is announced, I want to estimate operational fallout quickly so I can prioritize response actions.
2. When leadership asks why a factory is at risk, I want an explainable causal chain instead of a black-box prediction.
3. When selling AI to factories, I want a vivid demo that turns geopolitical or supplier risk into a concrete operational story.

## Problem

Factories are pressured to "use AI" but most AI demos for operations are either dashboards, generic copilots, or ungrounded chat. They do not answer the practical question:

`What happens to this line if a supplier, route, or regulation changes tomorrow?`

Users need a fast and intuitive way to simulate cascading failure, identify the tipping point, and inspect recommended mitigations.

## Product Hypothesis

If we repurpose MiroShark's multi-agent simulation engine from public-opinion dynamics to operational cascade dynamics, then we can ship a polished hackathon demo that feels novel, useful, and commercially legible to factory owners without building a dashboard platform or a full forecasting product.

## First Slice Boundary

The first SLC slice is:

- one synthetic factory scenario
- one shock event
- one simulation run
- one generated risk brief
- one agent interrogation flow

The slice ends when a user can watch the system go from scenario input to operational recommendation in a single live path.

## Must-Have MVP Capabilities

1. Accept a factory scenario document that describes suppliers, materials, inventories, routes, and factory context.
2. Accept a shock prompt such as an export ban, supplier outage, or shipping delay.
3. Generate stakeholder agents grounded in the scenario.
4. Run a multi-round simulation of operational reactions and cascading effects.
5. Produce a report with:
   - failure chain
   - estimated disruption window / line-down proxy
   - most stressed dependencies
   - mitigation recommendations
6. Let the user inspect or chat with at least one relevant agent to explain the outcome.
7. Support a review loop with one primary shock and backup shocks so the team can rehearse and verify the same workflow repeatedly.
8. Save or surface a fallback artifact set for demo safety: cached run, saved report, or screenshots.

## Non-Goals

- Becoming a generic factory dashboard
- Becoming a generic factory copilot
- Real ERP, MES, or SAP integrations
- Real-time external data ingestion
- Precise probabilistic forecasting claims
- Full enterprise dashboarding
- Multi-factory portfolio optimization
- Production-grade auth, billing, or user management

## Constraints

- Must be built during the hackathon.
- Must be demoable live in about 3 minutes.
- MiroShark setup is already happening separately; leverage it rather than replacing it.
- Fake or synthetic factory data is allowed and preferable.
- Codex must be the backbone, not a cosmetic extra.
- Time to spec before autonomous execution is about 30 minutes.
- Verification should be delegated to a separate verifier/test-oriented agent whenever possible rather than self-certified by the implementing agent.

## Key Risks

1. The operational framing may not map cleanly onto MiroShark's current social-platform assumptions.
2. The team may overbuild custom UI instead of using existing report and interaction surfaces.
3. "Days until failure" could sound over-precise if the underlying model is obviously heuristic.
4. Simulation speed or model cost may make live demos brittle.
5. The demo may look impressive but not trustworthy to a factory owner if it cannot clearly explain the causal chain.

## Risk Response

1. Treat the output as a scenario simulator, not a forecasting oracle.
2. Prioritize report quality and agent explainability over bespoke visuals.
3. Use a narrow scenario with clear variables and a short round count.
4. Prepare a cached/fallback run for demo safety if needed.
5. Force the demo to show the causal chain, constrained node, and one agent explanation tied to the same scenario assumptions.

## UX Promise

The user should feel:

- fast comprehension of the situation
- confidence that the system can explain itself
- practical next steps rather than abstract AI language

The product should feel like a supply-chain risk decision tool, not a dashboard.

## Trust Signal

The strongest trust moment in the hackathon demo should be:

1. a grounded causal failure chain anchored in explicit scenario assumptions
2. one clearly identified constrained node or tipping point
3. one agent explanation that references the same shock and constraints
4. mitigation actions that are visibly linked back to that chain

## Success Criteria

The hackathon MVP is successful if, during a live demo, the user can:

1. Load a factory scenario and shock.
2. Run the simulation without manual debugging.
3. Show a generated brief with a clear causal chain.
4. Show an estimated disruption window or tipping point proxy.
5. Ask one agent why it reacted the way it did.
6. Explain why this matters for real factories in under 30 seconds.
7. Rehearse the workflow across a primary and backup shock without changing the product story.
8. Fall back to a saved report or cached run if the live path gets brittle without breaking the narrative.

## Demo Narrative

`A geopolitical or supplier shock hits. Instead of opening spreadsheets and Slack threads, the operator runs a simulation. In minutes, they see what fails first, how long they have, and which mitigation buys time.`

## Recommended Next Handoff

Use `spec-to-ticket` on a single demo slice focused on the end-to-end run:

- scenario input
- shock configuration
- simulation execution
- report output
- agent interrogation
