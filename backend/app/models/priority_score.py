from dataclasses import dataclass, field
from app.models.code_entity import CodeEntity

@dataclass
class PriorityScore:
    """
    Represents the calculated priority
    of a CodeEntity.
    """
    entity: CodeEntity
    complexity_points: int
    issue_points: int
    churn_points: int
    total_score: int
    reasoning: list[str] = field(default_factory=list)