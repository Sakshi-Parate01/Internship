from pydantic import BaseModel
from typing import List


class DocumentMetadata(BaseModel):
    filename: str
    file_type: str
    word_count: int
    cleaned_text: str


class IngestionResult(BaseModel):
    documents: List[DocumentMetadata]