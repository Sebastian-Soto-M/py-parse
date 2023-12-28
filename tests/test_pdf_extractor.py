import pytest
from pathlib import Path
from app import PDFExtractor

pdf_files = [
    Path('assets')/f'{i}.pdf' for i in ['ai_tips', 'ai_tips2', 'bitacora']
]

@pytest.mark.parametrize('pdf_path', pdf_files)
def test_extract_metadata(pdf_path):
    extractor = PDFExtractor(pdf_path)
    metadata = extractor.extract().metadata
    assert metadata is not None
    # Add more assertions related to metadata structure and content

@pytest.mark.parametrize('pdf_path', pdf_files)
def test_extract_text_content(pdf_path):
    extractor = PDFExtractor(pdf_path)
    text_content = extractor.extract().text_content
    assert isinstance(text_content, str)
    # Add more assertions about the text content

# Similarly, add tests for tables and images

