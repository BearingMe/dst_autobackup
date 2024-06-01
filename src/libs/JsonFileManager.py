import json
import os
from typing import Any


class JsonFileManager:
    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path

    @property
    def exists(self) -> bool:
        return os.path.exists(self.file_path) and os.path.isfile(self.file_path)

    def get(self, key: str) -> dict[str, Any]:
        with open(self.file_path, "r") as file:
            data = json.load(file)
            return data.get(key, None)
