# app/models.py
from pydantic import BaseModel
from typing import Optional


class DocumentResult(BaseModel):
    filename: str
    content_length: int
    language: Optional[str]