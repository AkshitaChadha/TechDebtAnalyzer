from pathlib import Path

class Settings:

    BASE_DIR = Path(__file__).resolve().parents[2]

    REPOSITORIES_DIR = BASE_DIR / "repositories"

    REPORTS_DIR = BASE_DIR / "reports"
    def __init__(self):

        self.REPOSITORIES_DIR.mkdir(exist_ok=True)

        self.REPORTS_DIR.mkdir(exist_ok=True)


settings = Settings()
