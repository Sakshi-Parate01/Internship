# app/processors/pdf_processor.py
from PyPDF2 import PdfReader
from .base import Processor
import os


class PDFProcessor(Processor):

    async def process(self):
        print("Processing file:", self.filepath)
        print("File exists:", os.path.exists(self.filepath))
        print("File size:", os.path.getsize(self.filepath))
        reader = PdfReader(self.filepath)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

 