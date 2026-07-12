from app.models.analysis_result import AnalysisResult
from app.models.priority_score import PriorityScore

from app.services.priority.scoring import (
    complexity_points,
    issue_points,
    churn_points,
)

def calculate_priority_scores(
    analysis: AnalysisResult,
) -> None:
    """
    Calculate deterministic priority scores for every CodeEntity.
    """
    analysis.priority_scores.clear()
    for entity in analysis.entities:
        complexity_score = complexity_points(
            entity.complexity or 0
        )
        issue_score = issue_points(
            entity.issues
        )
        churn_score = churn_points(
            entity.commit_count
        )
        total = (
            complexity_score
            + issue_score
            + churn_score
        )
        reasons = []
        if complexity_score > 5:
            reasons.append("High cyclomatic complexity")
        if issue_score > 0:
            reasons.append(
                f"{len(entity.issues)} static analysis issue(s)"
            )
        if churn_score > 5:
            reasons.append("Frequently modified")
        analysis.priority_scores.append(
            PriorityScore(
                entity=entity,
                complexity_points=complexity_score,
                issue_points=issue_score,
                churn_points=churn_score,
                total_score=total,
                reasoning=reasons,
            )
        )
    analysis.priority_scores.sort(
        key=lambda score: score.total_score,
        reverse=True,
    )