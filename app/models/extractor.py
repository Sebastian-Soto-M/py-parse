from dataclasses import dataclass
from typing import Any, Optional
from .handlers import FileHandler


@dataclass
class ExtractedMetadata:
    metadata: Optional[dict[str, Any]]
    text_content: Optional[str]
    image_data: list[dict[str, Any]]
    tables: list[list[list[str]]]


class Extractor:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler

    def get_metadata(self) -> Optional[Any]:
        return self.file_handler.extract_metadata()

    def get_content(self):
        return self.file_handler.extract_content()
