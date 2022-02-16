"""Core workflow for CRISPR Guide Checker by Red@."""

PROJECT_NAME = "CRISPR Guide Checker"
DOMAIN_THEME = "bioinformatics"


def build_snapshot() -> dict[str, str]:
    return {"project": PROJECT_NAME, "author": "Red@", "theme": DOMAIN_THEME}
