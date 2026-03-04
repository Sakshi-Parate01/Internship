import os
import json
from app.readers import read_file
from app.cleaner import clean_text
from app.models import DocumentMetadata, IngestionResult
from app.utils import get_files_from_folder


# Paths
INPUT_FOLDER = "data/input"
OUTPUT_FILE = "output/results.json"

# Dummy classes for illustration
# Replace with your Pydantic models
class DocumentMetadata:
    def __init__(self, filename, file_type, word_count, cleaned_text):
        self.filename = filename
        self.file_type = file_type
        self.word_count = word_count
        self.cleaned_text = cleaned_text

    def model_dump(self):
        return self.__dict__

class IngestionResult:
    def __init__(self, documents):
        self.documents = documents

    def model_dump(self):
        return {"documents": [doc.model_dump() for doc in self.documents]}


# Dummy functions for illustration
def read_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def clean_text(text):
    return text.strip()  # simple cleaning example


# document processing
def process_documents():
    documents = []

    # Loop through all files in the input folder
    for filename in os.listdir(INPUT_FOLDER):
        print("Found file:", filename)

        file_path = os.path.join(INPUT_FOLDER, filename)

        try:
            # Read and clean the file
            raw_text = read_file(file_path)
            cleaned = clean_text(raw_text)

            # Create metadata
            metadata = DocumentMetadata(
                filename=filename,
                file_type=os.path.splitext(filename)[1],
                word_count=len(cleaned.split()),
                cleaned_text=cleaned
            )

            documents.append(metadata)

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    # Save results to JSON
    result = IngestionResult(documents)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(result.model_dump(), f, indent=4)

    print("Processing complete. Output saved to results.json")


if __name__ == "__main__":
    process_documents()