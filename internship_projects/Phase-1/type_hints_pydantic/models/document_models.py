from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
from datetime import datetime


# 1. Document Input Model

class DocumentInput(BaseModel):
    filename: str = Field(..., min_length=3)
    content: str = Field(..., min_length=10)
    file_type: str = Field(..., pattern="^(pdf|txt|docx)$")
    uploaded_at: datetime

    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value: str) -> str:
        if "." not in value:
            raise ValueError("Filename must contain an extension.")
        return value


# 2. Processing Config Model

class ProcessingConfig(BaseModel):
    language: str = Field(default="en")
    remove_stopwords: bool = True
    min_word_length: int = Field(default=3, ge=1, le=15)
    enable_summarization: bool = False


# 3. Extraction Result Model

class ExtractionResult(BaseModel):
    filename: str
    word_count: int = Field(..., ge=0)
    detected_language: Optional[str] = None
    summary: Optional[str] = None
    keywords: List[str] = []

    @field_validator("keywords")
    @classmethod
    def validate_keywords(cls, value: List[str]) -> List[str]:
        for word in value:
            if not word.strip():
                raise ValueError("Keywords cannot contain empty strings.")
        return value