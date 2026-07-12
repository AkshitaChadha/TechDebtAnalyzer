from app.models.analysis_result import AnalysisResult
from app.models.churn_metric import ChurnMetric

def run_churn_stage(
    analysis: AnalysisResult,
    metrics: list[ChurnMetric],
) -> None:
    """
    Attach Git commit counts to CodeEntity objects.
    """
    churn_lookup = {}
    for metric in metrics:
        churn_lookup[metric.file_path] = metric.commit_count
    for entity in analysis.entities:
        entity.commit_count = churn_lookup.get(
            entity.file_path,
            0,
        )