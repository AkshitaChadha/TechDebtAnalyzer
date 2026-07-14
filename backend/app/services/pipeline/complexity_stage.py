from app.models.analysis_result import AnalysisResult
from app.models.complexity_metric import ComplexityMetric


def run_complexity_stage(
    analysis: AnalysisResult,
    metrics: list[ComplexityMetric],
) -> None:
    """
    Attach complexity metrics to their corresponding CodeEntity objects.
    """

    complexity_lookup = {}

    for metric in metrics:
        #print( metric.file_path, metric.line, metric.complexity)
        key = (
            metric.file_path,
            metric.line,
        )

        complexity_lookup[key] = metric.complexity

    for entity in analysis.entities:
        #print("ENTITY:", entity.file_path, entity.start_line,)
        key = (
            entity.file_path,
            entity.start_line,
        )

        if key in complexity_lookup:
            entity.complexity = complexity_lookup[key]