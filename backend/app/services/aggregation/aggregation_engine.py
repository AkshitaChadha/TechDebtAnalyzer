from collections import defaultdict

from app.models.repository import Repository
from app.models.repository_file import RepositoryFile
from app.models.repository_function import RepositoryFunction


class AggregationEngine:

    def build_repository(self, entities):
        files = {}

        for entity in entities:
            path = entity.file_path

            if path not in files:
                files[path] = RepositoryFile(path=path)

            files[path].functions.append(
                RepositoryFunction(
                    name=entity.name,
                    file_path=entity.file_path,
                    entity_type=entity.entity_type,
                    complexity=entity.complexity.cyclomatic_complexity,
                    issues=entity.issues,
                    start_line=entity.start_line,
                    end_line=entity.end_line,
                )
            )

        return Repository(files=list(files.values()))