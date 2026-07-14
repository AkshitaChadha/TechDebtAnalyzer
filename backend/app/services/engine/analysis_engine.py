from pathlib import Path

from app.models.analysis_result import AnalysisResult

from app.services.analysis.repository_scanner import get_python_files
from app.services.analysis.ast_parser import extract_code_entities
from app.services.analysis.complexity import analyze_complexity
from app.services.analysis.static_analysis import run_static_analysis

from app.services.pipeline.complexity_stage import run_complexity_stage
from app.services.pipeline.issue_stage import run_issue_stage
from app.services.pipeline.churn_stage import run_churn_stage

from app.services.git.churn import analyze_code_churn

from app.services.priority.priority_engine import (
    calculate_priority_scores,
)

from app.services.aggregation.aggregation_engine import (
    AggregationEngine,
)


def analyze_repository(repository_path: Path) -> AnalysisResult:
    """
    Executes the complete repository analysis pipeline.
    """

    analysis = AnalysisResult(
        repository_name=repository_path.name,
        repository_path=repository_path,
    )

    # ----------------------------
    # Scan Repository
    # ----------------------------

    analysis.python_files = get_python_files(
        repository_path
    )

    complexity_metrics = []

    # ----------------------------
    # File-Level Analysis
    # ----------------------------

    for file in analysis.python_files:

        analysis.entities.extend(
            extract_code_entities(file)
        )

        complexity_metrics.extend(
            analyze_complexity(file)
        )

    # ----------------------------
    # Repository-Level Analysis
    # ----------------------------

    issues = run_static_analysis(
        repository_path
    )

    churn_metrics = analyze_code_churn(
        repository_path
    )

    # ----------------------------
    # Pipeline Stages
    # ----------------------------

    run_complexity_stage(
        analysis,
        complexity_metrics,
    )

    run_issue_stage(
        analysis,
        issues,
    )

    run_churn_stage(
        analysis,
        churn_metrics,
    )

    analysis.issues = issues

    aggregation_engine = AggregationEngine()

    repository = aggregation_engine.build_repository(
        analysis.entities
    )

    calculate_priority_scores(
        analysis,
        repository,
    )

    return analysis