from app.models.code_entity import CodeEntity


def attach_complexity(
    entities: list[CodeEntity],
    complexities: list[dict],
) -> None:
    """
    Attach Radon complexity metrics to existing CodeEntity objects.
    """

    complexity_lookup = {}

    for item in complexities:
        key = (
            item["file_path"],
            item["line"],
        )

        complexity_lookup[key] = item["complexity"]

    for entity in entities:
        key = (
            entity.file_path,
            entity.start_line,
        )

        if key in complexity_lookup:
            entity.complexity = complexity_lookup[key]