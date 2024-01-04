from dataclasses import dataclass
import logging
from typing import Any, Optional

from app.models.content import Content
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
        self.logger = logging.getLogger(Extractor.__class__.__name__)

    def get_metadata(self) -> Optional[dict[str, Any]]:
        try:
            return self.file_handler.extract_metadata()
        except FileNotFoundError as fne:
            self.logger.error(fne)

    def get_content(self) -> Optional[Content]:
        try:
            return self.file_handler.extract_content()
        except FileNotFoundError as fne:
            self.logger.error(fne)
