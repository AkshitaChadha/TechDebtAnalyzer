from app.models.repository import Repository
from app.models.repository_file import RepositoryFile
from app.models.repository_function import RepositoryFunction


class AggregationEngine:
    """
    Groups CodeEntity objects into RepositoryFile objects
    and computes file-level metrics.
    """

    def build_repository(self, entities):
        files = {}

        # ----------------------------
        # Group entities by file
        # ----------------------------
        for entity in entities:

            path = entity.file_path

            if path not in files:
                files[path] = RepositoryFile(
                    path=path,
                )

            files[path].functions.append(
                RepositoryFunction(
                    name=entity.name,
                    file_path=entity.file_path,
                    entity_type=entity.entity_type,
                    complexity=entity.complexity or 0,
                    commit_count=entity.commit_count,
                    issues=entity.issues,
                    start_line=entity.start_line,
                    end_line=entity.end_line,
                )
            )

        # ----------------------------
        # Compute file-level metrics
        # ----------------------------
        for repo_file in files.values():

            repo_file.max_complexity = max(
                (
                    function.complexity
                    for function in repo_file.functions
                ),
                default=0,
            )

            if repo_file.functions:
                repo_file.average_complexity = (
                    sum(
                        function.complexity
                        for function in repo_file.functions
                    )
                    / len(repo_file.functions)
                )

            repo_file.static_findings = sum(
                len(function.issues)
                for function in repo_file.functions
            )

            # Git churn is already file-level.
            # Every function in the file has the same value.
            repo_file.git_churn = max(
                function.commit_count
                for function in repo_file.functions
            )

            repo_file.complex_function_count = sum(
                1
                for function in repo_file.functions
                if function.complexity >= 10
            )

        # ----------------------------
        # Return aggregated repository
        # ----------------------------
        return Repository(
            files=list(files.values())
        )