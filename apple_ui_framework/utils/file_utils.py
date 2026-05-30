from pathlib import Path


def create_directory(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def safe_name(value: str) -> str:
    return (
        value.replace("/", "_")
        .replace("\\", "_")
        .replace(":", "_")
        .replace(" ", "_")
        .replace("[", "")
        .replace("]", "")
    )
