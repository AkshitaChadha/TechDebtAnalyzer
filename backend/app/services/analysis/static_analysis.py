import json
import subprocess
from pathlib import Path

from app.adapters.ruff_adapter import normalize_ruff_issues


def run_static_analysis(repository_path: Path):
    """
    Run all static analysis tools on the repository.

    Version 1:
    - Ruff
    """

    result = subprocess.run(
        [
            "ruff",
            "check",
            str(repository_path),
            "--output-format",
            "json",
        ],
        capture_output=True,
        text=True,
    )

    if not result.stdout:
        return []

    raw = json.loads(result.stdout)

    return normalize_ruff_issues(raw)

