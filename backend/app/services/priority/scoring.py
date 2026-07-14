from app.models.issue import Issue


def complexity_points(complexity: int) -> int:
    """
    Convert cyclomatic complexity into weighted points.
    """

    if complexity <= 5:
        level = "LOW"

    elif complexity <= 10:
        level = "MODERATE"

    elif complexity <= 20:
        level = "HIGH"

    else:
        level = "VERY_HIGH"

    complexity_weights = {
        "LOW": 2,
        "MODERATE": 5,
        "HIGH": 10,
        "VERY_HIGH": 15,
    }

    return complexity_weights[level]


def issue_points(issues: list[Issue]) -> int:
    """
    Calculate maintainability points.
    """

    points = 0
    for issue in issues:
        if issue.category == "style":
            continue

        if issue.category == "correctness":
            continue
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