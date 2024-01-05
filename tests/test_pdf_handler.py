import logging
import pytest
from app.models.content import ContentWithImage

from app.models.handlers import PDFHandler
from tests import get_assets_path

files_dict = get_assets_path('pdf')
files_list = files_dict.values()
logger = logging.getLogger('pdf_handler')


def test_fail_extract_metadata():
    handler = PDFHandler('invalid path')
    with pytest.raises(FileNotFoundError):
        handler.extract_metadata()


@pytest.mark.parametrize('files', files_list)
def test_extract_metadata(files):
    md = PDFHandler(files).extract_metadata()
    assert md
    assert len(md.keys()) > 0
    # with pytest.raises(NoPropertiesError) as e:
    #     extractor.get_metadata()
    # Add more assertions related to metadata structure and content


@pytest.mark.parametrize('files', files_list)
def test_extract_text_content(files):
    content = PDFHandler(files).extract_content()
    logger.info(content)
    assert isinstance(content, ContentWithImage)
    text = content.text
    assert isinstance(text, str)
    # Add more assertions about the text content


def test_extract_table_metadata():
    f = files_dict['bitacora']
    content = PDFHandler(f).extract_content()
    assert content
    assert len(content.tables) > 0
