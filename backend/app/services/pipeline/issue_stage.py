from app.models.analysis_result import AnalysisResult
from app.models.issue import Issue

def run_issue_stage(
    analysis: AnalysisResult,
    issues: list[Issue],
) -> None:
    """
    Attach issues to their corresponding CodeEntity objects.
    """
    issue_lookup = {}
    for issue in issues:
        key = (
            issue.file_path,
            issue.line,
        )
        issue_lookup.setdefault(key, []).append(issue)
    for entity in analysis.entities:
        key = (
            entity.file_path,
            entity.start_line,
        )
        if key in issue_lookup:
            entity.issues.extend(issue_lookup[key])