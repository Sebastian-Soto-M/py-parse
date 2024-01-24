from tika import parser

from .handler import FileHandler
from tika import parser


class TikaHandler(FileHandler):
    def __init__(self, filename):
        super().__init__(filename)

    def get_content(self) -> str:
        """
        Parse the content of a file using Apache Tika and return the text content.

        :param file_path: Path to the file to be parsed.
        :param key: could be 'content' (default) | 'metadata'
        :return: A string containing the parsed text content or None if an error occurs or content is not available.
        """
        parsed_data = parser.from_file(str(self.file))
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
        return text
