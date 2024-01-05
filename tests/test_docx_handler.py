import logging
import pytest
from app.exceptions import NoPropertiesError
from app.models.content import Content

from app.models.extractor import Extractor
from app.models.handlers import DOCXHandler
from tests import get_assets_path

files_dict = get_assets_path('docx')
files_list = files_dict.values()
logger = logging.getLogger('docx_handler')


def test_fail_extract_metadata():
    handler = DOCXHandler('invalid path')
    with pytest.raises(FileNotFoundError):
        handler.extract_metadata()


@pytest.mark.parametrize('files', files_list)
def test_extract_metadata(files):
    handler = DOCXHandler(files)
    md = handler.extract_metadata()
    assert md
    logger.info(md)
    assert len(md.keys()) > 0


@pytest.mark.parametrize('files', files_list)
def test_extract_text_content(files):
    content = DOCXHandler(files).extract_content()
    logger.info(content.text)
    logger.info(content.tables)
    assert isinstance(content, Content)
    # Add more assertions about the text content
