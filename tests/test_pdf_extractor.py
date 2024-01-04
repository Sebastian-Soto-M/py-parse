import pytest
from app.exceptions import NoPropertiesError
from app.models.content import ContentWithImage

from app.models.extractor import Extractor
from app.models.handlers import PDFHandler
from tests import get_assets_path

files = get_assets_path('pdf')


@pytest.mark.parametrize('file_path', files)
def test_extract_metadata(file_path):
    extractor = Extractor(PDFHandler(file_path))
    with pytest.raises(NoPropertiesError) as e:
        extractor.get_metadata()
    # Add more assertions related to metadata structure and content


@pytest.mark.parametrize('file_path', files)
def test_extract_text_content(file_path):
    content = Extractor(PDFHandler(file_path)).get_content()
    assert isinstance(content, ContentWithImage)
    text = content.text
    assert isinstance(text, str)
    # Add more assertions about the text content
