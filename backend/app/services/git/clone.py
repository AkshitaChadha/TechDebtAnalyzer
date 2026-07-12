from pathlib import Path
from git import GitCommandError, Repo

from app.core.config import settings
from app.exceptions import RepositoryCloneError
from app.utils import logger

def clone_repository(repo_url: str) -> Path:
    """
    Clone a GitHub repository into the local repositories directory.
    """

    # Extract repository name
    repo_name = repo_url.rstrip("/").split("/")[-1].replace(".git", "")

    # Destination path
    destination = settings.REPOSITORIES_DIR / repo_name

    # Already cloned?
    if destination.exists():
        logger.info(
            f"Repository already exists: {destination}"
        )

        return destination
    
    # Clone repository
    try:
        Repo.clone_from(repo_url, destination)
        logger.info("Repository cloned successfully.")

    except GitCommandError:
        logger.error("Repository cloning failed.")
        raise RepositoryCloneError(
            "Repository could not be cloned. "
            "Please check the URL or repository permissions."
        )
    return destination