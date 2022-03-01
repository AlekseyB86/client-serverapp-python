import os
import re
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
INFO_FILES_DIR = BASE_DIR.joinpath('info_files')

def get_files(directory, file_extension=None):
    all_files = os.listdir(directory)
    for file in all_files:
        if re.search(file_extension, file):
            yield file