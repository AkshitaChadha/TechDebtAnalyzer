from pathlib import Path

from app.dto.analysis_response import build_analysis_response
from app.models.analysis_result import AnalysisResult
from app.models.code_entity import CodeEntity
from app.models.entity_type import EntityType
from app.models.priority_score import PriorityScore


def test_analysis_response_structure():

    entity = CodeEntity(
        name="dashboard",
        entity_type=EntityType.FUNCTION,
        file_path=Path("dashboard.py"),
        start_line=10,
        end_line=50,
        complexity=20,
        commit_count=15,
    )

    priority = PriorityScore(
        entity=entity,
        complexity_points=15,
        issue_points=0,
        churn_points=5,
        total_score=20,
        reasoning=["High cyclomatic complexity"],
    )

    analysis = AnalysisResult(
        repository_name="Demo",
        repository_path=Path("."),
    )
    analysis.entities.append(entity)
    analysis.priority_scores.append(priority)
    response = build_analysis_response(analysis)
    assert "repository" in response
    assert "summary" in response
    assert "roadmap" in response
    assert response["repository"]["name"] == "Demo"
    assert len(response["roadmap"]) == 1
    assert response["roadmap"][0]["entity"] == "dashboard"