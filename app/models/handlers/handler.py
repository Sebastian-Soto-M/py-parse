from typing import Optional, Any
import logging
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Optional
from app.models.content import Content


class FileHandler(ABC):
    def __init__(self, filename: str):
        self.file = Path(filename)
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def extract_metadata(self) -> Optional[dict[str, Any]]:
        raise NotImplementedError

    @abstractmethod
    def extract_content(self) -> Content:
        raise NotImplementedError


class ImageHandler(FileHandler):
    def extract_metadata(self):
        # Logic to extract image metadata
        return "Image Metadata"

    def extract_content(self):
        # Logic to extract image content
        return "Image Content"
