from typing import List, Dict, Any


class Content:
    def __init__(self, text: str, tables: list[list[list[str]]]):
        self.text = text
        self.tables = tables


class ContentWithImage(Content):
    def __init__(self, text: str, tables: list[list[list[str]]], images: list[dict[str, Any]]):
        """
        initializes the pdfcontent object with text, table data, and image data.

        :param text: extracted text content from the pdf.
        :param tables: extracted table data from the pdf, as a list of tables.
        :param images: extracted image data from the pdf, as a list of image metadata.
        """
        super().__init__(text, tables)
        self.images = images
