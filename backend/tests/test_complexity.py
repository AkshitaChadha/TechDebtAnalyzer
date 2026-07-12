from app.services.analysis.complexity import analyze_complexity


def test_complexity_detection(tmp_path):
    """
    Verify that Radon detects cyclomatic complexity.
    """

    sample = tmp_path / "sample.py"

    sample.write_text(
        """
def example(x):
    if x > 0:
        print(x)
    else:
        print(-x)
"""
    )

    result = analyze_complexity(sample)

    assert len(result) == 1

    # analyze_complexity() now returns ComplexityMetric objects
    assert result[0].complexity > 1