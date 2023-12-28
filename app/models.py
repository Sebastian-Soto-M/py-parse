from abc import abstractmethod, ABC
from pathlib import Path
from dataclasses import dataclass
from typing import Any, Optional

@dataclass
class ExtractedMetadata:
    metadata: Optional[dict[str, Any]]
    text_content: Optional[str]
    image_data: list[dict[str, Any]]
    tables: list[list[list[str]]]


class Extractor(ABC):
    def __init__(self, file_path: Path):
        self.file_path = file_path

    @abstractmethod
    def extract(self) -> ExtractedMetadata:
        raise NotImplementedError

