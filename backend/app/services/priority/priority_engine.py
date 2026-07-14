from app.models.analysis_result import AnalysisResult
from app.models.priority_score import PriorityScore
from app.models.repository import Repository

from app.services.priority.scoring import (
    complexity_points,
    issue_points,
    churn_points,
)


def calculate_priority_scores(
    analysis: AnalysisResult,
    repository: Repository,
) -> None:
    """
    Calculate file-level priority scores.
    """

    analysis.priority_scores.clear()

    for repo_file in repository.files:

        # Representative function (highest complexity)
        representative = max(
            repo_file.functions,
            key=lambda function: function.complexity,
        )

        # ----------------------------
        # Scores
        # ----------------------------
        complexity_score = complexity_points(
            repo_file.max_complexity
        )

        all_issues = [
            issue
            for function in repo_file.functions
            for issue in function.issues
        ]

        issue_score = issue_points(
            all_issues
        )

        churn_score = churn_points(
            repo_file.git_churn
        )

        maintainability_score = (
            complexity_score
            + issue_score
        )

        total_score = (
            maintainability_score
            + churn_score
        )

        # ----------------------------
        # Reasons
        # ----------------------------
        quality_reasons = []

        if repo_file.max_complexity >= 10:
            quality_reasons.append(
                "Contains highly complex function(s)"
            )

        if repo_file.static_findings > 0:
            quality_reasons.append(
                f"{repo_file.static_findings} maintainability finding(s)"
            )

        priority_reasons = []

        if repo_file.git_churn >= 20:
            priority_reasons.append(
                "High change activity"
            )

        reasons = (
            quality_reasons
            + priority_reasons
        )
        
        # ----------------------------
        # Recommendation Gate
        # ----------------------------
        needs_refactoring = (
            repo_file.max_complexity >= 10
            or repo_file.static_findings > 0
        )

        if not needs_refactoring:
            continue

        # ----------------------------
        # Store Result
        # ----------------------------
        analysis.priority_scores.append(
            PriorityScore(
                entity=representative,
                complexity_points=complexity_score,
                issue_points=issue_score,
                churn_points=churn_score,
                total_score=total_score,
                reasoning=reasons,
            )
        )

    # ----------------------------
    # Sort by priority
    # ----------------------------
    analysis.priority_scores.sort(
        key=lambda score: score.total_score,
        reverse=True,
    )