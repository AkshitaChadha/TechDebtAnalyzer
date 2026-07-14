from dataclasses import dataclass
from pathlib import Path
from dataclasses import dataclass

@dataclass
class Issue:
    tool: str
    code: str
    message: str
    severity: str
    file_path: Path
    line: int
    category:str= "maintainability"