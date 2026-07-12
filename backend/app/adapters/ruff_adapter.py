from pathlib import Path
from app.models.issue import Issue

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
            )
        )
    return issues