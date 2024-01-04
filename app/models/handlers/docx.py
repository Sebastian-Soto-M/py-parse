from typing import Any, Optional
from pdfminer.psparser import PSException
from docx.api import Document
from zipfile import ZipFile
from app.exceptions import NoPropertiesError
from app.models.content import Content
from app.models.handlers import FileHandler


class DOCXHandler(FileHandler):

    def extract_metadata(self) -> Optional[dict[str, Any]]:
        try:
            metadata = {}
            with ZipFile(self.file, 'r') as docx:
                with docx.open('docProps/core.xml') as file:
                    tree = ET.parse(file)
                    root = tree.getroot()

                    for element in root:
                        for key in ns.keys():
                            ns_key = f"{{{ns[key]}}}"
                            if ns_key in element.tag:
                                tag = element.tag.split(ns_key)[1]
                                metadata[tag] = element.text
        except PSException as e:
            self.logger.error(e)

    def extract_content(self) -> Content:
        def _extract_text(doc) -> str:
            return '\n'.join([para.text for para in doc.paragraphs])

        def _extract_tables(doc) -> list:
            tables = []
            for table in doc.tables:
                table_content = []
                for row in table.rows:
                    # this character will be the column divider.
                    row_content = "|".join([cell.text for cell in row.cells])
                    table_content.append(row_content)
                tables.append(table_content)
            return tables

        doc = Document(str(self.file))
        text = _extract_text(doc)
        tables = _extract_tables(doc)
        return Content(text, tables)
