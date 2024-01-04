import pytest
from app.exceptions import NoPropertiesError
from app.models.content import Content

from app.models.extractor import Extractor
from app.models.handlers import DOCXHandler
from tests import get_assets_path

files = get_assets_path('docx')


def test_fail_extract_metadata():
    handler = DOCXHandler('invalid path')
    with pytest.raises(FileNotFoundError):
        handler.extract_metadata()


# @pytest.mark.parametrize('file_path', files)
# def test_extract_metadata(file_path):
#     handler = DOCXHandler(file_path)
#     assert handler.extract_metadata() is not None


@pytest.mark.parametrize('file_path', files)
def test_extract_text_content(file_path):
    content = DOCXHandler(file_path).extract_content()
    assert isinstance(content, Content)
    # Add more assertions about the text content
