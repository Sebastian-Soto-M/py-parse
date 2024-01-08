from typing import Any, Optional
from functools import partial
from tika import parser

from app.models.content import Content
from .handler import FileHandler
from tika import parser

from typing import Any, Tuple, Dict, Optional


class GenericHandler(FileHandler):
    def __init__(self, filename):
        super().__init__(filename)

    def extract_content(self) -> Content:
        """
        Parse the content of a file using Apache Tika and return the text content.

        :param file_path: Path to the file to be parsed.
        :param key: could be 'content' (default) | 'metadata'
        :return: A string containing the parsed text content or None if an error occurs or content is not available.
        """
        parsed_data = parser.from_file(self.file)
        text = ''
        if isinstance(parsed_data, tuple):
            # Handling the tuple return type
            status_code, content = parsed_data
            if status_code == 200 and content:
                text = content.strip()
        elif isinstance(parsed_data, dict):
            # Handling the dictionary return type
            content = parsed_data['content']
            if content:
                text = content.strip()
        return Content(text=text)

    def extract_metadata(self) -> dict[str, Any]:
        parsed_data = parser.from_file(self.file)
        if isinstance(parsed_data, tuple):
            # Handling the tuple return type
            status_code, content = parsed_data
            if status_code == 200 and content:
                return content
        elif isinstance(parsed_data, dict):
            # Handling the dictionary return type
            metadata = parsed_data['metadata']
            return metadata
