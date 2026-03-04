import re


def clean_text(text: str) -> str:
    # Remove extra spaces
    text = re.sub(r"\s+", " ", text)

    # Remove special characters (basic cleaning)
    text = re.sub(r"[^\w\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    return text.strip()