from typing import Any, Optional
from .models import ExtractedMetadata, Extractor
import pdfplumber

class PDFExtractor(Extractor):

    def _open_pdf(self) -> Optional[pdfplumber.pdf.PDF]:
        try:
            return pdfplumber.open(self.file_path)
        except Exception as e:
            print(f"Error opening PDF file: {e}")
            return None

    def _extract_metadata(self, pdf) -> dict[str, Any]:
        return pdf.metadata if pdf else {}

    def _extract_text_content(self, pdf) -> str:
        text_content = ''
        if pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    text_content += text + '\n'
        return text_content.strip()

    def _extract_tables(self, pdf) -> list[list[list[str]]]:
        all_tables = []
        if pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    all_tables.append(table)
        return all_tables

    def _extract_image_data(self, pdf) -> list[dict[str, Any]]:
        image_info = []
        if pdf:
            for page in pdf.pages:
                for img in page.images:
                    image_info.append(img)
        return image_info

    def extract(self) -> ExtractedMetadata:
        with self._open_pdf() as pdf:
            return ExtractedMetadata(
                metadata=self._extract_metadata(pdf),
                text_content=self._extract_text_content(pdf),
                tables=self._extract_tables(pdf),
                image_data=self._extract_image_data(pdf)
            )