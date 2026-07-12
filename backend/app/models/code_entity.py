from dataclasses import dataclass, field

from pathlib import Path

from app.models.entity_type import EntityType
from app.models.issue import Issue


@dataclass
class CodeEntity:
    name: str
    entity_type: EntityType
    file_path: Path
    start_line: int
    end_line: int
    parent: str | None = None
    complexity: int | None = None
    commit_count: int = 0
    issues: list[Issue] = field(default_factory=list)
    priority_score: float | None = None