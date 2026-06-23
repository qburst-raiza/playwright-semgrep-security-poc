import json
import os
from pathlib import Path
from typing import Any


DATA_DIR = Path(__file__).parent.parent / "data"


def load_json(filename: str) -> Any:
    file_path = DATA_DIR / filename
    with open(file_path, encoding="utf-8") as f:
        return json.load(f)


def get_test_data(key: str) -> Any:
    data = load_json("test_data.json")
    keys = key.split(".")
    result = data
    for k in keys:
        result = result[k]
    return result


def get_env(key: str, default: str = "") -> str:
    return os.getenv(key, default)
