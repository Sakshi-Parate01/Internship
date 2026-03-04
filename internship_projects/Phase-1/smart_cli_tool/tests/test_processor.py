import pytest
from app.processor import FileProcessor
from unittest.mock import patch


def test_process_files(sample_folder):
    processor = FileProcessor(str(sample_folder))
    results = processor.process_files()

    assert len(results) == 2
    assert results[0]["word_count"] > 0


def test_folder_not_exists():
    processor = FileProcessor("wrong_path")

    with pytest.raises(FileNotFoundError):
        processor.process_files()


@patch("os.listdir")
def test_mocked_listdir(mock_listdir):
    mock_listdir.return_value = ["file1.txt"]

    processor = FileProcessor("dummy_path")

    with patch("os.path.exists", return_value=True):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.__enter__.return_value.read.return_value = "mocked content"

            results = processor.process_files()

            assert results[0]["word_count"] == 2