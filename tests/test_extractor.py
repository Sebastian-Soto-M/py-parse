from app.models.extractor import FileDetails, Extractor
from app.models.handlers.pdf import PDFHandler
from tests import get_assets_path


def test_extractor_invalid_file_path():
    ext = Extractor(PDFHandler('N/A'))
    assert ext.get_metadata() is None


def test_extractor_call():
    filepath = get_assets_path('pdf')['03-Sistemas de Correo y Agenda 3']
    ext = Extractor(PDFHandler(filepath))
    data = ext()
    assert isinstance(data, FileDetails)
