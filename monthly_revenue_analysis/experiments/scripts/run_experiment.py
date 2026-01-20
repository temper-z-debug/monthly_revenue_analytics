from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Dict

import yaml

# Ensure repo modules are importable
THIS_FILE = Path(__file__).resolve()
EXPERIMENTS_DIR = THIS_FILE.parents[1]   # .../experiments
REPO_ROOT = THIS_FILE.parents[2]         # .../monthly_revenue_analysis(github)

sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(EXPERIMENTS_DIR / "src"))

from sim.experiment import run_bootstrap_uq, run_copula_rho_sweep, run_decision_threshold

def load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    parser = argparse.ArgumentParser(description="Run research-style experiments (copula / bootstrap UQ / decision threshold).")
    parser.add_argument("--config", required=True, help="Path to YAML config.")
    args = parser.parse_args()

    cfg_path = (REPO_ROOT / args.config) if not Path(args.config).is_absolute() else Path(args.config)
    cfg_path = cfg_path.resolve()
    if not cfg_path.exists():
        raise FileNotFoundError(f"Config not found: {cfg_path}")

    cfg = load_yaml(cfg_path)
    name = cfg.get("experiment", {}).get("name")
    if name == "copula_rho_sweep":
        bundle = run_copula_rho_sweep(cfg)
    elif name == "bootstrap_uq":
        bundle = run_bootstrap_uq(cfg)
    elif name == "decision_threshold":
        bundle = run_decision_threshold(cfg)
    else:
        raise ValueError(f"Unknown experiment name: {name}")

    print("\n[OK] Experiment finished")
    print(f"Output dir: {bundle.out_dir}")
    print(f"results.csv: {bundle.results_csv}")
    print(f"metadata.json: {bundle.metadata_json}\n")


if __name__ == "__main__":
    main()
