import pytest
from app.models.content import Content, ContentWithImage

from app.models.extractor import Extractor
from app.models.handlers import PDFHandler

files = [
    f'assets/{i}.pdf' for i in ['ai_tips', 'ai_tips2', 'bitacora']
]


@pytest.mark.parametrize('file_path', files)
def test_extract_metadata(file_path):
    metadata = Extractor(PDFHandler(file_path)).get_metadata()
    breakpoint()
    assert metadata is not None
    # Add more assertions related to metadata structure and content


@pytest.mark.parametrize('file_path', files)
def test_extract_text_content(file_path):
    content = Extractor(PDFHandler(file_path)).get_content()
    assert isinstance(content, ContentWithImage)
    text = content.text
    breakpoint()
    assert isinstance(text, str)
    # Add more assertions about the text content
