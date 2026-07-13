from dataclasses import dataclass, field
from typing import List

from app.models.repository_function import RepositoryFunction


@dataclass
class RepositoryFile:
    path: str

    functions: List[RepositoryFunction] = field(default_factory=list)

    git_churn: int = 0
    static_findings: int = 0

    max_complexity: int = 0
    average_complexity: float = 0.0
    complex_function_count: int = 0