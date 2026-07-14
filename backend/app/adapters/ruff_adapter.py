from pathlib import Path
from app.models.issue import Issue
from app.core.constants import RUFF_CATEGORY_MAP

def classify_issue_category(code: str) -> str:
    """
    Classify a Ruff issue into an engineering category.
    """

    # Exact match
    if code in RUFF_CATEGORY_MAP:
        return RUFF_CATEGORY_MAP[code]

    # Prefix match
    for prefix, category in RUFF_CATEGORY_MAP.items():
        if code.startswith(prefix):
            return category

    return "maintainability"
def normalize_ruff_issues(raw_issues: list[dict]) -> list[Issue]:
    issues = []
    for issue in raw_issues:
        issues.append(

            Issue(
            tool="ruff",
            code=issue["code"],
            message=issue["message"],
            severity=issue["severity"],
            file_path=Path(issue["filename"]),
            line=issue["location"]["row"],
            category=classify_issue_category(
                issue["code"]
            ),
        )
        )
    return issues