import logging

import pytest

from tests import get_assets_path

from app.models.handlers import TikaHandler
from app.models.parser import Parser

files_dict = get_assets_path('pdf')
files_list = files_dict.values()
logger = logging.getLogger('pdf_handler')


@pytest.mark.parametrize('files', files_list)
def test_parser(files):
    p = Parser(TikaHandler(files))
    s = p.get_content()
    assert len(s) > 0
