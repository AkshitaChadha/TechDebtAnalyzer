from dataclasses import dataclass, field
from typing import List
from app.models.repository_file import RepositoryFile

@dataclass
class Repository:
    files: List[RepositoryFile] = field(default_factory=list)