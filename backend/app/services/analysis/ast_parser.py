import ast
from pathlib import Path

from app.models.code_entity import CodeEntity
from app.models.entity_type import EntityType


class CodeEntityVisitor(ast.NodeVisitor):
    """
    Visits the AST and extracts classes, functions, and methods.
    """

    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.entities: list[CodeEntity] = []

    def visit_ClassDef(self, node: ast.ClassDef):

        self.entities.append(
            CodeEntity(
                name=node.name,
                entity_type=EntityType.CLASS,
                file_path=self.file_path,
                start_line=node.lineno,
                end_line=node.end_lineno,
            )
        )

        self.generic_visit(node)

    def visit_FunctionDef(self, node: ast.FunctionDef):

        if isinstance(node.parent, ast.ClassDef):
            entity_type = EntityType.METHOD
            parent = node.parent.name
        else:
            entity_type = EntityType.FUNCTION
            parent = None

        self.entities.append(
            CodeEntity(
                name=node.name,
                entity_type=entity_type,
                file_path=self.file_path,
                start_line=node.lineno,
                end_line=node.end_lineno,
                parent=parent,
            )
        )

        self.generic_visit(node)


def extract_code_entities(file_path: Path) -> list[CodeEntity]:
    """
    Extract code entities from a Python source file.
    """

    source = file_path.read_text(encoding="utf-8")

    tree = ast.parse(source)

    # Attach parent references
    for parent in ast.walk(tree):
        for child in ast.iter_child_nodes(parent):
            child.parent = parent

    visitor = CodeEntityVisitor(file_path)

    visitor.visit(tree)

    return visitor.entities