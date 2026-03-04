import argparse
from app.processor import FileProcessor
from app.logger_config import setup_logger


def main():
    setup_logger()

    parser = argparse.ArgumentParser(
        description="Process text files in a folder"
    )

    parser.add_argument(
        "folder",
        type=str,
        help="Path to folder containing text files"
    )

    args = parser.parse_args()

    processor = FileProcessor(args.folder)
    results = processor.process_files()

    print("Results:")
    for r in results:
        print(r)


if __name__ == "__main__":
    main()