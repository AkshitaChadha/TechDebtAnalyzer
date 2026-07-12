from app.services.git.clone import clone_repository
from app.services.engine.analysis_engine import analyze_repository
from pprint import pprint
from app.dto.analysis_response import build_analysis_response

REPO_URL = "https://github.com/AkshitaChadha/CodeVerseAI"


def main():

    print("=" * 60)
    print("RefactorIQ Developer Runner")
    print("=" * 60)

    # -------------------------------
    # Clone Repository
    # -------------------------------
    print("\nCloning repository...")

    repo_path = clone_repository(REPO_URL)

    print("Done!")

    # -------------------------------
    # Run Analysis Engine
    # -------------------------------
    print("\nRunning analysis...")

    analysis = analyze_repository(repo_path)
    response = build_analysis_response(analysis)
    print("Done!")

    # -------------------------------
    # Display Repository Summary
    # -------------------------------
    print("\nGenerated API Response\n")
    pprint(response)
    
if __name__ == "__main__":
    main()