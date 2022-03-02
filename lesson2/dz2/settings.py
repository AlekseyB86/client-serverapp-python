from datetime import datetime
import os
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
INFO_FILES_DIR = BASE_DIR.joinpath('info_files')

ORDER = {
    'item': 'iphone 13 PRO',
    'quantity': '300',
    'price': '116900.5',
    'buyer': 'Маршал',
    'date': datetime.now().strftime("%d-%m-%Y, %H-%M-%S"),
}
ORDERS = [ORDER, ]

DATA_TO_YAML = {
    '1€': [1, 'python', 0.2],
    '2€': 2,
    '3€': ORDER
}

def get_files(directory, file_extension=None):
    all_files = os.listdir(directory)
    for file in all_files:
        if re.search(file_extension, file):
            yield file



