#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/run_factory_shock_demo.py

echo
echo "Demo bundle refreshed."
echo "Open these assets:"
echo "  - docs/demo-assets/fallback-artifacts/report-fallback.html"
echo "  - docs/demo-assets/fallback-artifacts/interaction-fallback.html"
echo "  - docs/demo-assets/fallback-artifacts/screens/home.png"
