"""
Application-wide constants.
"""

# Number of roadmap items returned by the API
TOP_ROADMAP_ITEMS = 10

# Minimum score considered "high priority"
HIGH_PRIORITY_THRESHOLD = 20

# Priority scoring thresholds
LOW_COMPLEXITY = 5
MEDIUM_COMPLEXITY = 10
HIGH_COMPLEXITY = 20

LOW_CHURN = 5
MEDIUM_CHURN = 20
HIGH_CHURN = 50

RUFF_CATEGORY_MAP = {
    # ---------- Maintainability ----------
    "F401": "maintainability",   # unused import
    "F841": "maintainability",   # unused variable
    "SIM": "maintainability",    # simplify
    "UP": "maintainability",     # pyupgrade

    # ---------- Correctness ----------
    "F821": "correctness",       # undefined name
    "F823": "correctness",       # local variable referenced before assignment
    "B": "correctness",          # bugbear

    # ---------- Style ----------
    "E": "style",
    "W": "style",
}