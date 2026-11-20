#!/usr/bin/env bash
# Runs every program and refreshes outputs/ and figures/. Usage: bash run_all.sh
set -e
export MPLBACKEND=Agg
mkdir -p outputs figures
for f in code/Task_*.py modified/Task_*.py; do
  name=$(basename "$f" .py)
  echo "Running $name"
  (cd "$(dirname "$f")" && python3 "$name.py" > "../outputs/$name.txt" 2>&1)
done
echo "Done. Outputs are in outputs/ and figures in figures/."
