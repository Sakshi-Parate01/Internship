from dotenv import load_dotenv
import os
from datetime import datetime
from models.document_models import (
    DocumentInput,
    ProcessingConfig,
    ExtractionResult,
)

# Load environment variables
load_dotenv()

DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")

# Create input document
doc = DocumentInput(
    filename="report.pdf",
    content="This is a sample document used for testing.",
    file_type="pdf",
    uploaded_at=datetime.now(),
)

# Create processing config
config = ProcessingConfig(language=DEFAULT_LANGUAGE)

# Simulate processing
word_count = len(doc.content.split())

result = ExtractionResult(
    filename=doc.filename,
    word_count=word_count,
    detected_language=config.language,
    summary="Short generated summary.",
    keywords=["sample", "document", "validation"],
)

# Serialize to JSON
print(result.model_dump_json(indent=2))