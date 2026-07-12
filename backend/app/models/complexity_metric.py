from dataclasses import dataclass
from pathlib import Path

@dataclass
class ComplexityMetric:
    """
    Represents the cyclomatic complexity
    of a single function or class.
    """
    file_path: Path
    name: str
    line: int
    complexity: int