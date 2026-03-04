# app/cli.py
import argparse
import os
import asyncio
import json
import logging

from app.logger_config import setup_logger
from app.processors.txt_processor import TXTProcessor
from app.processors.pdf_processor import PDFProcessor
from app.api_client import APIClient
from app.models import DocumentResult


async def handle_file(filepath):
    if filepath.endswith(".txt"):
        processor = TXTProcessor(filepath)
    elif filepath.endswith(".pdf"):
        processor = PDFProcessor(filepath)
    else:
        logging.warning(f"Unsupported file: {filepath}")
        return None

    content = await processor.process()

    print(repr(content))
    print(len(content))

    api = APIClient()
    language = await api.detect_language(content[:500])

    result = DocumentResult(
        filename=os.path.basename(filepath),
        content_length=len(content),
        language=language
    )

    return result.model_dump()


async def main(folder_path):
    tasks = []

    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        tasks.append(handle_file(full_path))

    results = await asyncio.gather(*tasks)

    results = [r for r in results if r]

    os.makedirs("output", exist_ok=True)

    with open("output/results.json", "w") as f:
        json.dump(results, f, indent=4)

    logging.info("Processing completed!")


if __name__ == "__main__":
    setup_logger()

    parser = argparse.ArgumentParser()
    parser.add_argument("folder", help="Path to folder with documents")

    args = parser.parse_args()

    asyncio.run(main(args.folder))