import json
from pathlib import Path
from typing import Generator, List


class IndexLoader:
    @classmethod
    def load(cls, filepath: Path) -> dict:
        with open(filepath) as f:
            body: dict = json.load(f)
        return body


class TextLoadInterator:
    def __init__(self, filepath: Path) -> None:
        self._filepath = filepath

    def __iter__(self) -> Generator[str, None, None]:
        with open(self._filepath) as f:
            for line in f:
                yield line.strip()
