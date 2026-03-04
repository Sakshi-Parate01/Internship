import os
import logging

logger = logging.getLogger(__name__)


class FileProcessor:
    def __init__(self, folder_path: str):
        self.folder_path = folder_path

    def process_files(self):
        if not os.path.exists(self.folder_path):
            raise FileNotFoundError("Folder does not exist")

        results = []

        for filename in os.listdir(self.folder_path):
            if filename.endswith(".txt"):
                file_path = os.path.join(self.folder_path, filename)
                logger.info(f"Processing file: {filename}")

                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                    word_count = len(content.split())

                    results.append({
                        "filename": filename,
                        "word_count": word_count
                    })

        logger.info("Processing completed")
        return results