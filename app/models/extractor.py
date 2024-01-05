from dataclasses import dataclass
import logging
from typing import Any, Optional

from app.models.content import Content, ContentWithImage
from .handlers import FileHandler


@dataclass
class FileDetails:
    metadata: Optional[dict[str, Any]] = None
    text: Optional[str] = None
    images: Optional[list[dict[str, Any]]] = None
    tables: Optional[list[str]] = None


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

    def __call__(self) -> FileDetails:
        """Extracts the content and metadata from the file using the specified handler

        Returns:
            E: _description_
        """
        content = self.get_content()
        metadata = self.get_metadata()
        dtls = FileDetails(metadata=metadata)
        if content:
            dtls.text = content.text
            dtls.tables = content.tables
            dtls.images = content.images if isinstance(
                content, ContentWithImage) else None
        return dtls
