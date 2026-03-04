import os


def get_files_from_folder(folder_path: str):
    files = []
    for filename in os.listdir(folder_path):
        full_path = os.path.join(folder_path, filename)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files