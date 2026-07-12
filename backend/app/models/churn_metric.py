from dataclasses import dataclass
from pathlib import Path

@dataclass
class ChurnMetric:
    """
    Represents the change frequency of a file.
    """
    file_path: Path
    commit_count: int
    