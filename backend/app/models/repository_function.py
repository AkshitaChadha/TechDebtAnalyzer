from dataclasses import dataclass, field
from typing import List

from app.models.issue import Issue
from app.models.entity_type import EntityType


@dataclass
class RepositoryFunction:
    name: str
    file_path: str
    entity_type: EntityType

    complexity: int = 0
    commit_count: int = 0          # <-- ADD THIS

    issues: List[Issue] = field(default_factory=list)

    start_line: int | None = None
    end_line: int | None = None