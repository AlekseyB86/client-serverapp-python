"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
   info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
    Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
    считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения
    параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка — например,
    os_prod_list, os_name_list, os_code_list, os_type_list. В этой же функции создать главный список для хранения
    данных отчета — например, main_data — и поместить в него названия столбцов отчета в виде списка:
    «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
    Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);

    Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
    В этой функции реализовать получение данных через вызов функции get_data(), а также сохранение подготовленных
    данных в соответствующий CSV-файл;

    Проверить работу программы через вызов функции write_to_csv().
"""

import re
import csv

import numpy
from chardet import detect
from settings import INFO_FILES_DIR, get_files


def get_encoding_file(file_name: str) -> any:
    with open(file_name, 'rb') as f:
        content = f.read()
    return detect(content)['encoding']


def get_data() -> list:
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [os_prod_list, os_name_list, os_code_list, os_type_list]
    headers = [
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы'
    ]
    prod_pattern = re.compile(fr'{headers[0]}:\s*\S*')
    name_pattern = re.compile(fr'{headers[1]}:\s*\S*')
    code_pattern = re.compile(fr'{headers[2]}:\s*\S*')
    type_pattern = re.compile(fr'{headers[3]}:\s*\S*')

    for file in get_files(INFO_FILES_DIR, '.txt'):
        with open(INFO_FILES_DIR.joinpath(file), 'rb') as f:
            content = f.read()
            enc = detect(content)
            de_content = content.decode(enc['encoding'])

        os_prod_list.append(prod_pattern.findall(de_content)[0].split()[2])
        os_name_list.append(name_pattern.findall(de_content)[0].split()[2])
        os_code_list.append(code_pattern.findall(de_content)[0].split()[2])
        os_type_list.append(type_pattern.findall(de_content)[0].split()[2])

    main_data = numpy.array(main_data, dtype=object).T.tolist()
    main_data.insert(0, headers)
    return main_data


def write_to_csv(data: list) -> None:
    with open('task1_result', 'w', encoding='utf-8') as f_csv:
        f_writer = csv.writer(f_csv)
        f_writer.writerows(data)


if __name__ == '__main__':
    write_to_csv(get_data())
