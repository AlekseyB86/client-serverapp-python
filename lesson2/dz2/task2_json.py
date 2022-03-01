"""
2. Задание на закрепление знаний по модулю json. Есть файл orders в формате JSON с информацией о заказах.
Написать скрипт, автоматизирующий его заполнение данными. Для этого:

Создать функцию write_order_to_json(), в которую передается 5 параметров —
 - товар (item),
 - количество (quantity),
 - цена (price),
 - покупатель (buyer),
 - дата (date).
 Функция должна предусматривать запись данных в виде словаря в файл orders.json. При записи данных указать величину
 отступа в 4 пробельных символа;

Проверить работу программы через вызов функции write_order_to_json() с передачей в нее значений каждого параметра.
"""

import json

from settings import INFO_FILES_DIR, get_files, ORDERS


def write_order_to_json(orders: list) -> None:
    files = get_files(INFO_FILES_DIR, '.json')
    for file in files:
        with open(INFO_FILES_DIR.joinpath(file), 'r') as f:
            content = f.read()

        js_content = json.loads(content)
        js_content['orders'].extend(orders)
        with open(INFO_FILES_DIR.joinpath(file), 'w', encoding='utf-8') as f_n:
            json.dump(js_content, f_n, sort_keys=True, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    write_order_to_json(ORDERS)
