from app.models.entity_type import EntityType

from app.services.git.clone import clone_repository
from app.services.analysis.repository_scanner import get_python_files
from app.services.analysis.ast_parser import extract_code_entities


def run_analysis(repo_url: str):

    repo_path = clone_repository(repo_url)

    python_files = get_python_files(repo_path)

    all_entities = []

    for python_file in python_files:
        all_entities.extend(extract_code_entities(python_file))

    functions = sum(
        1
        for entity in all_entities
        if entity.entity_type == EntityType.FUNCTION
    )

    methods = sum(
        1
        for entity in all_entities
        if entity.entity_type == EntityType.METHOD
    )

    classes = sum(
        1
        for entity in all_entities
        if entity.entity_type == EntityType.CLASS
    ) 

    return {
        "repository": repo_path.name,
        "python_files": len(python_files),
        "functions": functions,
        "methods": methods,
        "classes": classes,
    }