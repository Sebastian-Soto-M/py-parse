from app.models.extractor import FileDetails, Extractor
from app.models.handlers.docx import DOCXHandler
from app.models.handlers.pdf import PDFHandler
from app.models.handlers.pptx import PPTXHandler
from tests import get_assets_path


def test_extractor_invalid_file_path():
    ext = Extractor(PDFHandler('N/A'))
    assert ext.get_metadata() is None


def test_extractor_call_docx():
    filepath = get_assets_path('docx')['text and tables']
    ext = Extractor(DOCXHandler(filepath))
    data = ext()
    assert isinstance(data, FileDetails)


def test_extractor_call_pptx():
    filepath = get_assets_path('pdf')['03-Sistemas de Correo y Agenda 3']
    ext = Extractor(PDFHandler(filepath))
    data = ext()
    assert isinstance(data, FileDetails)


def test_extractor_call_pdf():
    filepath = get_assets_path('pptx')['ppt_template']
    ext = Extractor(PPTXHandler(filepath))
    data = ext()
    assert isinstance(data, FileDetails)
