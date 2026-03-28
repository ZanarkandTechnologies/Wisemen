# Blockers And Bypasses

## Purpose

Track the likely places where the autonomous build can stall and define the cheapest bypass for each.

## Current Known Questions

### 1. How do files get into MiroShark?

- Status: answered
- Route: multipart POST to `/api/graph/ontology/generate`
- Fields: `files`, `simulation_requirement`, optional `project_name`, optional `additional_context`
- Bypass: use direct `curl` if the UI upload flow is flaky

### 2. Is MiroShark actually running right now?

- Status: uncertain
- Why it matters: all autonomous build work depends on a reachable run path
- Latest check in this session: `curl` to `http://localhost:5001/health` and `http://localhost:3000` failed from this shell after the user's earlier successful checks
- Bypass now: re-verify before each major runtime-dependent task
- Human help now: none required unless the service only exists in a separate inaccessible environment

### 3. Which surface should carry the payoff?

- Status: unresolved
- Preferred answer: reuse the existing report page
- Autonomous fallback: use the existing report and lightly adapt labels before building a new dashboard
- Human help now: only needed if you want to force a very specific visual style

### 4. Where does `days until disruption` come from?

- Status: unresolved
- Risk: overclaiming exactness
- Autonomous fallback: phrase as `estimated disruption window` or derive a heuristic from inventory and lead-time assumptions
- Human help now: not required

### 5. Can the engine meaningfully simulate factory stakeholders without deep backend changes?

- Status: likely yes, but unproven
- Autonomous plan: test with one synthetic scenario and operationally worded simulation requirement
- Bypass: if deep behavior still feels social, keep the run path and shift the demo framing to `agentic operational scenario exploration`

### 6. What if runtime is too slow for a live demo?

- Status: likely risk
- Autonomous fallback:
  - shorten rounds
  - reduce stakeholders
  - cache one successful run
  - pre-save screenshots and report output
- Human help now: none required

### 7. What if the frontend is flaky but the backend works?

- Status: expected possible failure mode
- Autonomous fallback:
  - drive the backend APIs directly
  - inspect saved artifacts and generated project data
  - keep the demo focused on the output artifact

### 8. What if credentials or model setup are incomplete?

- Status: possible
- Autonomous fallback:
  - use the currently working provider path
  - avoid changing model topology during the hackathon
- Human help now: provide missing keys or confirm the intended provider only if the existing setup fails

## Things The Human Can Help With Right Now

These are optional accelerators, not blockers:

1. Confirm the preferred live payoff surface: existing report page vs thin custom summary.
2. Confirm whether you want heuristic wording instead of exact `days until failure`.
3. If services stop again, restart the known-good MiroShark process in the environment you are using.

## Things The Agent Should Figure Out Later Autonomously

1. Whether operational relabeling alone is enough or small report-copy changes are needed.
2. Whether the direct API path is more reliable than the UI upload path.
3. Which minimum stakeholder set yields the best demo-to-runtime ratio.
4. Which fallback artifacts are needed after the first successful run.
