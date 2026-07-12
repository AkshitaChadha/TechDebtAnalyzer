from dataclasses import dataclass, field
from pathlib import Path

from app.models.code_entity import CodeEntity
from app.models.issue import Issue
from app.models.priority_score import PriorityScore

@dataclass
class AnalysisResult:
    """
    Stores everything discovered during repository analysis.

    Every stage of the analysis pipeline enriches this object.
    """

    repository_name: str
    repository_path: Path
    python_files: list[Path] = field(default_factory=list)
    entities: list[CodeEntity] = field(default_factory=list)
    issues: list[Issue] = field(default_factory=list)
    priority_scores: list[PriorityScore] = field(default_factory=list)