from fastapi import APIRouter, HTTPException
from app.schemas.analysis import RepositoryRequest
from app.dto.analysis_response import build_analysis_response
from app.services.git.clone import clone_repository
from app.services.engine.analysis_engine import analyze_repository
from app.exceptions import (
    RepositoryCloneError,
    RepositoryAnalysisError,
)
router = APIRouter()
@router.post("/analyze")
def analyze(request: RepositoryRequest):
    """
    Analyze a GitHub repository and return
    the RefactorIQ roadmap.
    """

    try:
        repo_path = clone_repository(
            str(request.repo_url)
        )
        analysis = analyze_repository(
            repo_path
        )
        return build_analysis_response(
            analysis
        )
    except RepositoryCloneError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )
    except RepositoryAnalysisError as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Unexpected server error.",
        )