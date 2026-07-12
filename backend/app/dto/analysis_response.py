from app.models.analysis_result import AnalysisResult

from app.core.constants import (
    TOP_ROADMAP_ITEMS,
    HIGH_PRIORITY_THRESHOLD,
)
def build_analysis_response(
    analysis: AnalysisResult,
) -> dict:
    """
    Convert AnalysisResult into the API response
    expected by the frontend.
    """

    return {
        "repository": {
            "name": analysis.repository_name,
            "python_files": len(analysis.python_files),
        },

        "summary": {
            "entities": len(analysis.entities),
            "issues": len(analysis.issues),

            "high_priority_items": sum(
                1
                for priority in analysis.priority_scores
                if priority.total_score >= HIGH_PRIORITY_THRESHOLD
            ),

            "highest_priority_score": (
                analysis.priority_scores[0].total_score
                if analysis.priority_scores
                else 0
            ),
        },

        "roadmap": [

            {
                "rank": index + 1,

                "entity": priority.entity.name,
                "entity_type": priority.entity.entity_type.value,
                "file": priority.entity.file_path.name,
                "start_line": priority.entity.start_line,
                "end_line": priority.entity.end_line,
                "total_score": priority.total_score,
                "breakdown": {
                    "complexity": {
                        "cyclomatic_complexity": priority.entity.complexity,
                        "points": priority.complexity_points,
                    },
                    "issues": {
                        "count": len(priority.entity.issues),
                        "points": priority.issue_points,
                    },

                    "churn": {
                        "commits": priority.entity.commit_count,
                        "points": priority.churn_points,
                    },
                },

                "reasons": priority.reasoning,
            }

            for index, priority in enumerate(
                analysis.priority_scores[:TOP_ROADMAP_ITEMS]
            )
        ],
    }