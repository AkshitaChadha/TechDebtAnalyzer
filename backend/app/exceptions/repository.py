class RepositoryCloneError(Exception):
    """
    Raised when cloning a repository fails.
    """
    pass


class RepositoryAnalysisError(Exception):
    """
    Raised when repository analysis fails.
    """
    pass