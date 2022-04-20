from io import BytesIO
from tika import parser
import re

def pdf_by_io(pdf_file):
    file = parser.from_buffer(BytesIO(pdf_file))['content']
    return file

def pdf_content_to_string(pdf_io):
    pdf = str(pdf_io)
    pdf = re.sub(r'\n', '', pdf)
    pdf = re.sub('  ', '', pdf)
    return pdf
