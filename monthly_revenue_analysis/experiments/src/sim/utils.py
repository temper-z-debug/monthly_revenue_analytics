from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional


def repo_root() -> Path:
    p = Path(__file__).resolve()
    return p.parents[4]


def utc_timestamp() -> str:
    return datetime.utcnow().strftime("%Y%m%d_%H%M%S")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def write_json(path: Path, obj: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


@dataclass
class OutputBundle:
    out_dir: Path
    results_csv: Path
    metadata_json: Path


def make_output_bundle(output_root: Path, exp_name: str) -> OutputBundle:
    stamp = utc_timestamp()
    out_dir = output_root / f"{stamp}_{exp_name}"
    out_dir.mkdir(parents=True, exist_ok=True)
    return OutputBundle(
        out_dir=out_dir,
        results_csv=out_dir / "results.csv",
        metadata_json=out_dir / "metadata.json",
    )


def try_get_git_commit(repo: Path) -> Optional[str]:
    head = repo / ".git" / "HEAD"
    if not head.exists():
        return None
    try:
        ref = head.read_text(encoding="utf-8").strip()
        if ref.startswith("ref:"):
            rel = ref.split(" ", 1)[1].strip()
            ref_path = repo / ".git" / rel
            if ref_path.exists():
                return ref_path.read_text(encoding="utf-8").strip()
        return ref
    except Exception:
        return None
