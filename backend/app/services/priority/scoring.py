from app.models.issue import Issue


def complexity_points(complexity: int) -> int:
    """
    Convert cyclomatic complexity into weighted points.
    """

    if complexity <= 5:
        return 2

    if complexity <= 10:
        return 5

    if complexity <= 20:
        return 10

    return 15


def issue_points(issues: list[Issue]) -> int:
    """
    Calculate points based on issue severity.
    """

    points = 0

    for issue in issues:

        severity = issue.severity.lower()

        if severity == "error":
            points += 5

        elif severity == "warning":
            points += 3

        else:
            points += 1

    return points


def churn_points(commit_count: int) -> int:
    """
    Convert Git churn into weighted points.
    """

    if commit_count <= 5:
        return 1

    if commit_count <= 20:
        return 5

    if commit_count <= 50:
        return 10
    return 15