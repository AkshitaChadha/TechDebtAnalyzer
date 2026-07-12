import pytest

from app.exceptions import RepositoryCloneError
from app.services.git.clone import clone_repository


def test_invalid_repository():
    """
    Verify that an invalid GitHub repository
    raises RepositoryCloneError.
    """

    with pytest.raises(RepositoryCloneError):
        clone_repository(
            "https://github.com/this-user/this-repository-does-not-exist"
        )