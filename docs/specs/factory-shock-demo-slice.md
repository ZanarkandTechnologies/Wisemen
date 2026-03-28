# Spec: Factory Shock Simulator Demo Slice

## Slice Name

`single-scenario operational shock simulation`

## Slice Goal

Turn one synthetic factory scenario plus one shock into a live, explainable simulation demo that ends in an operational mitigation brief.

## Why This Slice

This is the smallest slice that proves the core product claim without requiring enterprise integrations or a brand-new simulation engine.

## Demo User Stories

### Story 1: Configure the scenario

As a solutions engineer, I can load a synthetic factory scenario so the system has enough context to simulate an operational cascade.

Acceptance criteria:

- There is one prepared factory scenario document suitable for demo.
- The scenario clearly names the factory, major inputs, suppliers, routes, and baseline inventory assumptions.
- The simulation prompt is written in operational language rather than public-opinion language.

### Story 2: Inject a shock

As a user, I can specify a concrete shock event so the simulation has a crisp causal trigger.

Acceptance criteria:

- At least one primary shock is demo-ready.
- The shock is concrete and easy to understand in one sentence.
- The shock can plausibly affect cost, lead time, or throughput.

Suggested primary shock:

- `China restricts lithium precursor exports for 30 days, doubling lead times and increasing cost volatility.`

Suggested backup shocks:

- `A Tier-1 supplier quality issue pauses separator shipments for 10 days.`
- `A port disruption delays inbound battery materials by 14 days.`

Concrete prompt files:

- `docs/demo-assets/primary-shock-prompt.md`
- `docs/demo-assets/backup-shock-separator-pause.md`
- `docs/demo-assets/backup-shock-port-delay.md`

## Scenario Matrix For Review Loops

The autonomous review loop should reuse a small fixed matrix so the team can verify the same workflow repeatedly:

| Case | Purpose | Expected payoff |
| --- | --- | --- |
| Lithium export restriction (primary) | Main live demo path | Clear causal chain from precursor delay to line-down risk |
| Separator shipment pause | Backup verification path | Demonstrates single-point supplier fragility |
| Port disruption delay | Backup verification path | Demonstrates logistics delay and cost/throughput tradeoff |

### Story 3: Run the simulation

As a user, I can trigger a simulation run and observe that multiple stakeholders react to the same shock from different incentives.

Acceptance criteria:

- A run can start from the prepared scenario without manual code edits.
- The simulation includes at least 4 meaningful stakeholder roles.
- The system produces a visible timeline, run state, or report-ready output.

Minimum stakeholder set:

- procurement lead
- plant manager
- logistics coordinator
- supplier account manager
- optional: regulator or OEM customer

### Story 4: See the operational brief

As a user, I receive a concise output that explains what breaks first, when risk becomes critical, and what mitigation actions matter most.

Acceptance criteria:

- The output names the top causal chain.
- The output gives a disruption window or line-down proxy.
- The output provides at least 3 mitigation actions.
- The output language is operational and decision-oriented.
- The output identifies the most constrained node or tipping point clearly enough to say out loud in the demo.

Required output fields:

- `Primary failure chain`
- `Estimated time to disruption`
- `Most constrained node`
- `Cost / delay / throughput effects`
- `Recommended actions`

### Story 5: Interrogate one agent

As a user, I can click or query one agent and ask why it made its decision.

Acceptance criteria:

- At least one agent interaction path works reliably.
- The answer references the scenario and the shock, not generic advice.
- The interaction strengthens trust in the report.
- The answer ties back to the same constrained node, mitigation tradeoff, or failure chain shown in the brief.

Recommended demo agent:

- procurement lead or supplier account manager

## Demo Script Target

### Opening

`This is a battery materials factory. We gave the system its supply graph and a shock: lithium precursor exports get restricted.`

### Middle

`Codex uses MiroShark's simulation engine to model how procurement, logistics, suppliers, and the plant react over time.`

### Payoff

`The system shows the estimated disruption window, the failure chain, and the cheapest actions to buy time.`

### Trust moment

`We can ask the procurement agent why it escalated the risk and inspect its reasoning.`

The trust moment must connect three things in one chain:

1. scenario assumption
2. simulated failure chain
3. agent explanation or mitigation recommendation

## Manual Setup Checklist For Right Now

1. Prepare one synthetic scenario document in plain language.
2. Prepare one primary shock and two backups.
3. Decide the exact prompt text that maps MiroShark into operational mode.
4. Confirm the cheapest working run path in the current setup.
5. Confirm how the estimated disruption window / line-down proxy is derived and phrased.
6. Prepare one fallback artifact: screenshot set, saved report, or cached run.
7. Define the verifier-agent review loop for the scenario matrix.

Fallback staging location:

- `docs/demo-assets/fallback-artifacts/`

## Autonomous Review Loop

After each meaningful change, use this loop:

1. Run the primary shock scenario.
2. Delegate verification to a separate verifier/test-oriented agent.
3. If the primary path is flaky, run one backup scenario or inspect a cached artifact.
4. Check the acceptance bar:
   - top causal chain is legible
   - disruption/risk window is legible
   - mitigation actions are present
   - one agent explanation is grounded in the same shock
5. Save evidence: report link, screenshot set, or cached output.

## Scope Guardrails

- Do not build a full factory dashboard.
- Do not chase external integrations.
- Do not add multi-scenario comparison unless the first end-to-end loop already works.
- Do not overpromise numerical accuracy.
- Do not turn the product into a generic copilot.
- Do not let UI polish outrun the risk-analysis workflow.

## Payoff Surface Decision

- Primary payoff surface: reuse the existing report page.
- Allowed enhancement: a thin enterprise wrapper or summary shell if it clarifies the factory-owner story.
- Not allowed: a large custom dashboard rewrite before the core run path is stable.

## Demo Safety Decision

- Live path is preferred.
- Cached successful runs, saved reports, and screenshot walkthroughs are valid fallback artifacts.
- Backup shocks should preserve the same product story rather than introducing a second narrative.

## Disruption Window Decision

- Phrase the output as an **estimated disruption window / line-down proxy**, not an exact forecast.
- Derive it from the scenario assumptions, inventory burn, lead-time expansion, and throughput risk.
- If the underlying simulation does not expose a clean numeric field, a lightweight post-processed heuristic is acceptable as long as the wording stays honest.

## Minimum Code-Change Decision

The minimum code-change set for judge-legible operational framing is:

1. relabel existing MiroShark user-facing copy from social-reaction language to operational-risk language
2. shape the report output so it clearly exposes:
   - primary failure chain
   - estimated disruption window / line-down proxy
   - constrained node
   - mitigation actions
3. keep one reliable agent interaction path available from the existing report/interaction flow
4. avoid deep backend rewrites unless those three changes still fail to make the demo legible

Preferred surfaces to adapt:

- existing report page
- existing interaction path
- existing upload / run flow

Defer until later:

- broad custom dashboard work
- deeper engine changes
- multi-scenario UX

## Open Questions To Resolve Before Ralph
- None at the product-direction level. Remaining questions should be handled in implementation planning, not requirements discovery.
