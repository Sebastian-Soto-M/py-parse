import pytest
from app.exceptions import NoPropertiesError
from app.models.content import Content

from app.models.extractor import Extractor
from app.models.handlers import DOCXHandler

files = [
    f'assets/{i}.docx' for i in ['test']
]


@pytest.mark.parametrize('file_path', files)
def test_extract_metadata(file_path):
    extractor = Extractor(DOCXHandler(file_path))
    with pytest.raises(NoPropertiesError) as e:
        extractor.get_metadata()


@pytest.mark.parametrize('file_path', files)
def test_extract_text_content(file_path):
    content = Extractor(DOCXHandler(file_path)).get_content()
    text = content.text
    assert isinstance(text, str)
    assert len(content.tables[0]) > 10
    # Add more assertions about the text content
