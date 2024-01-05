import logging
import pytest
from app.models.content import Content

from app.models.handlers import PPTXHandler
from tests import get_assets_path

files_dict = get_assets_path('pptx')
files_list = files_dict.values()
logger = logging.getLogger('pptx_handler')


def test_fail_extract_metadata():
    handler = PPTXHandler('invalid path')
    with pytest.raises(FileNotFoundError):
        handler.extract_metadata()


@pytest.mark.parametrize('files', files_list)
def test_extract_metadata(files):
    handler = PPTXHandler(files)
    md = handler.extract_metadata()
    assert md
    logger.info(md)
    assert len(md.keys()) > 0


@pytest.mark.parametrize('files', files_list)
def test_extract_text_content(files):
    content = PPTXHandler(files).extract_content()
    logger.info(content.text)
    logger.info(content.tables)
    assert isinstance(content, Content)
    # Add more assertions about the text content
