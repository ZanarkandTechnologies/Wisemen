# Troubles

Append repeated failures, brittle commands, and correction patterns here.

## 2026-03-28

- The user previously reported successful local checks for `http://localhost:5001/health` and `http://localhost:3000`, but later `curl` checks from this shell returned connection failures. Future agents should always re-verify service availability before assuming MiroShark is live.
