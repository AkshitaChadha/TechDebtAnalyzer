from app.services.analysis.static_analysis import run_static_analysis

def test_ruff_detects_unused_import(tmp_path):
    sample = tmp_path / "sample.py"
    sample.write_text(
        "import os\n"
    )
    issues = run_static_analysis(sample)
    assert len(issues) > 0
    assert issues[0].tool == "ruff"