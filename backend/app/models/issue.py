from dataclasses import dataclass
from pathlib import Path

@dataclass
class Issue:
    tool: str
    code: str
    message: str
    severity: str
    file_path: Path
    line: int