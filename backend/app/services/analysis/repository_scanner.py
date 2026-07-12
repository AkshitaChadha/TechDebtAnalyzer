from pathlib import Path


def get_python_files(repository_path: Path) -> list[Path]:
    """
    Recursively find all Python files in the repository.

    Args:
        repository_path: Path to the cloned repository.

    Returns:
        A list of Python file paths.
    """

    return list(repository_path.rglob("*.py"))