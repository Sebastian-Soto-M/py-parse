import logging
from .handlers import FileHandler


class Parser:
    def __init__(self, file_handler: FileHandler):
        self.file_handler = file_handler
        self.logger = logging.getLogger(Parser.__class__.__name__)

    def get_content(self) -> str:
        try:
            return self.file_handler.get_content()
        except FileNotFoundError as fne:
            self.logger.warning(fne)
            return ''
