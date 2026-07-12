from collections import defaultdict
from pathlib import Path
from git import Repo
from app.models.churn_metric import ChurnMetric

def analyze_code_churn(repository_path: Path) -> list[ChurnMetric]:
    """
    Count how many commits touched each Python file.
    """
    repo = Repo(repository_path)
    commit_counts = defaultdict(int)
    for commit in repo.iter_commits():
        for file in commit.stats.files:
            if file.endswith(".py"):
                commit_counts[file] += 1
    metrics = []
    for file, count in commit_counts.items():
        metrics.append(
            ChurnMetric(
                file_path=repository_path / file,
                commit_count=count,
            )
        )
    return metrics