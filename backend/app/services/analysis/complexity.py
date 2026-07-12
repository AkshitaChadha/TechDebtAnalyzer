from pathlib import Path

from radon.complexity import cc_visit

from app.models.complexity_metric import ComplexityMetric


def analyze_complexity(file_path: Path) -> list[ComplexityMetric]:
    """
    Analyze the cyclomatic complexity of a Python file.
    """

    source = file_path.read_text(encoding="utf-8")

    results = cc_visit(source)

    complexities = []

    for result in results:
        complexities.append(
            ComplexityMetric(
                file_path=file_path,
                name=result.name,
                line=result.lineno,
                complexity=result.complexity,
            )
        )

    return complexities