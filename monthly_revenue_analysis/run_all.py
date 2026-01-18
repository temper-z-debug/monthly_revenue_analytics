"""
run_all.py
One-click runner for the monthly revenue pipeline.

Usage:
    python run_all.py
    python run_all.py --save
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent

NUM_PREFIX = re.compile(r"^(\d{2})_.*\.py$")  # e.g., 01_xxx.py, 10_xxx.py


def collect_scripts(folder: Path):
    scripts = []
    if not folder.exists():
        return scripts

    for p in folder.glob("*.py"):
        m = NUM_PREFIX.match(p.name)
        if m:
            scripts.append((int(m.group(1)), p))
    scripts.sort(key=lambda x: x[0])
    return [p for _, p in scripts]


def run_script(script_path: Path, save_flag: bool):
    print("\n" + "=" * 80)
    print(f"▶ Running: {script_path.relative_to(ROOT)}")
    print("=" * 80)

    env = os.environ.copy()
    env["SAVE_ARTIFACTS"] = "1" if save_flag else "0"

    subprocess.run(
        [sys.executable, str(script_path)],
        env=env,
        check=True,
        cwd=str(ROOT),
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--save", action="store_true", help="Enable artifact saving")
    args = parser.parse_args()

    analysis_dir = ROOT / "analysis"
    modelling_dir = ROOT / "modelling"

    analysis_scripts = collect_scripts(analysis_dir)
    modelling_scripts = collect_scripts(modelling_dir)

    all_scripts = analysis_scripts + modelling_scripts

    if not all_scripts:
        raise RuntimeError(
            "No scripts found. Expected numbered scripts like '01_*.py' under "
            f"{analysis_dir} and {modelling_dir}."
        )

    print("\n====================================================")
    print("Monthly Revenue Analysis — One-click Pipeline Runner")
    print("====================================================")
    print(f"Working dir     : {ROOT}")
    print(f"SAVE_ARTIFACTS  : {args.save}")
    print(f"Analysis scripts: {len(analysis_scripts)}")
    print(f"Model scripts   : {len(modelling_scripts)}")
    print("Execution order :")
    for s in all_scripts:
        print(f"  - {s.relative_to(ROOT)}")
    print("====================================================")

    for s in all_scripts:
        run_script(s, args.save)

    print("\n✔ All scripts completed successfully.")


if __name__ == "__main__":
    main()
