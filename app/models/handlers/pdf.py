from typing import Any, Optional
from app.exceptions import NoPropertiesError
from app.models.content import Content, ContentWithImage
from app.models.handlers import FileHandler
from pdfplumber import open
from pdfminer.psparser import PSException
from pdfplumber.pdf import PDF
from datetime import datetime


class PDFHandler(FileHandler):
    """
    Class that handles getting information from a PDF

    If there's an exception or no data, you get an empty dictionary
    """

    def _parse_date(self, date):
        # Original date example = "D:20230116165046+01'00'"
        # Format the date string by removing 'D:' and replacing "'" with ""
        formatted_date = date[2:][:8]
        # Parse and convert to ISO 8601 format
        try:
            return datetime.strptime(formatted_date, '%Y%m%d').isoformat()
        except Exception as e:
            self.logger.error(e)
            return ""

    def extract_metadata(self) -> Optional[dict[str, Any]]:
        """
        Extracts metadata from the PDF file.
        Returns a dictionary containing metadata.
        """
        try:
            with open(self.file) as pdf:
                if isinstance(pdf, PDF):
                    return {key: self._parse_date(value) if "date" in key.lower() else value
                            for key, value in pdf.metadata.items()}
        except PSException as e:
            self.logger.error(e)

    def extract_content(self) -> Optional[Content]:
        """
        Extracts text, table, and image data from the PDF file.
        Returns a PDFContent object.
        """
        try:
            with open(self.file) as pdf:
                if pdf:
                    text_content = self._extract_text_content(pdf)
                    table_data = self._extract_table_data(pdf)
                    image_data = self._extract_image_data(pdf)

                    return ContentWithImage(text_content, table_data, image_data)
        except PSException as e:
            self.logger.error(e)

    def _extract_text_content(self, pdf: PDF) -> str:
        """ Extracts and returns textual content from the PDF. """
        return "\n".join(page.extract_text() or "" for page in pdf.pages).strip()

    def _extract_table_data(self, pdf: PDF) -> list[list[list[str]]]:
        """ Extracts and returns table data from the PDF. """
        all_tables = []
        for page in pdf.pages:
            tables = page.extract_tables()
            if tables:
                all_tables.extend(tables)
        return all_tables

    def _extract_image_data(self, pdf: PDF) -> list[dict[str, Any]]:
        """ Extracts and returns image data from the PDF. """
        return [img for page in pdf.pages for img in page.images]
