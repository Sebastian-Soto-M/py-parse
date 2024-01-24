import logging
from abc import ABC, abstractmethod
from pathlib import Path


class FileHandler(ABC):
    def __init__(self, filename: str):
        self.file = Path(filename)
        self.logger = logging.getLogger(self.__class__.__name__)

    @abstractmethod
    def get_content(self) -> str:
        raise NotImplementedError
