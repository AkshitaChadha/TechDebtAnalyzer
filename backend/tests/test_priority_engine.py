from pathlib import Path

from app.models.analysis_result import AnalysisResult
from app.models.code_entity import CodeEntity
from app.models.entity_type import EntityType
from app.services.priority.priority_engine import (
    calculate_priority_scores,
)
def test_priority_score_calculation():

    entity = CodeEntity(
        name="login",
        entity_type=EntityType.FUNCTION,
        file_path=Path("auth.py"),
        start_line=10,
        end_line=30,
        complexity=18,
        commit_count=25,
        issues=[],
    )

    analysis = AnalysisResult(
        repository_name="Demo",
        repository_path=Path("."),
    )

    analysis.entities.append(entity)
    calculate_priority_scores(analysis)
    assert len(analysis.priority_scores) == 1
    priority = analysis.priority_scores[0]
    assert priority.entity.name == "login"
    assert priority.complexity_points == 10
    assert priority.churn_points == 10
    assert priority.total_score == 20
    assert "High cyclomatic complexity" in priority.reasoning
    assert "Frequently modified" in priority.reasoning