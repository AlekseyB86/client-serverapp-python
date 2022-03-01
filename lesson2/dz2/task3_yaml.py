"""
3. Задание на закрепление знаний по модулю yaml. Написать скрипт, автоматизирующий сохранение данных
    в файле YAML-формата.
  Для этого:
    Подготовить данные для записи в виде словаря, в котором первому ключу соответствует список, второму — целое число,
    третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом,
    отсутствующим в кодировке ASCII (например, €);

    Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
    При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а также установить возможность
    работы с юникодом: allow_unicode = True;

    Реализовать считывание данных из созданного файла и проверить, совпадают ли они с исходными.
"""

import yaml

from settings import INFO_FILES_DIR, DATA_TO_YAML


def write_to_yaml(data: dict, filename: str) -> None:
    with open(INFO_FILES_DIR.joinpath(filename), 'w', encoding='utf-8') as f:
        yaml.dump(data, f, default_flow_style=False, allow_unicode=True)


def read_yaml(filename: str) -> dict:
    with open(INFO_FILES_DIR.joinpath(filename), encoding='utf-8') as f_r:
        return yaml.load(f_r, Loader=yaml.FullLoader)


if __name__ == "__main__":
    file_name = 'task3_res.yaml'
    write_to_yaml(DATA_TO_YAML, file_name)
    print(f'DATA_TO_YAML == {file_name}: {DATA_TO_YAML == read_yaml(file_name)}')
