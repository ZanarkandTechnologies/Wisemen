# Fallback Artifacts Staging

Use this directory to stage demo-safety evidence before or during Ralph execution.

## Goal

If the live path becomes brittle, the demo should still have one trustworthy fallback path.

## Minimum Artifact Set

1. `latest-report.md` or exported report copy
2. `screens/` screenshot set for:
   - uploaded scenario
   - simulation running or completed
   - report payoff
   - agent interrogation
3. `notes.md` with:
   - which shock was used
   - when the artifact was captured
   - whether it came from a live run or cached run

## Backup Shock Files

- `docs/demo-assets/primary-shock-prompt.md`
- `docs/demo-assets/backup-shock-separator-pause.md`
- `docs/demo-assets/backup-shock-port-delay.md`

## Ralph Launch Intent

Ralph should prefer the live run, but these artifacts are valid fallbacks when runtime is brittle.
