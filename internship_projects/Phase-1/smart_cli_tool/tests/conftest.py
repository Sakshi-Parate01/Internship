import pytest
from app.processor import FileProcessor


@pytest.fixture
def sample_folder(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("hello world")

    file2 = tmp_path / "file2.txt"
    file2.write_text("python testing is easy")

    return tmp_path
