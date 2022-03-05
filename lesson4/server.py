"""
Программа-сервер

1. Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    - клиент отправляет запрос серверу;
    - сервер отвечает соответствующим кодом результата.

   Клиент и сервер должны быть реализованы в виде отдельных скриптов, содержащих соответствующие функции.
   Функции сервера:
    - принимает сообщение клиента;
    - формирует ответ клиенту;
    - отправляет ответ клиенту;
    - имеет параметры командной строки:
        -p <port> — TCP-порт для работы (по умолчанию использует 7777);
        -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""

import json
import socket
import sys

import common.variables as cv
from common.utils import get_message, send_message


def process_client_message(message):
    """
    Обработчик сообщений от клиентов, принимает словарь - сообщение от клиента, проверяет корректность,
    возвращает словарь-ответ для клиента
    """
    if cv.ACTION in message and message[cv.ACTION] == cv.PRESENCE and cv.TIME in message \
            and cv.USER in message and message[cv.USER][cv.ACCOUNT_NAME] == 'Guest':
        return {cv.RESPONSE: 200}
    return {
        cv.RESPONDEFAULT_IP_ADDRESSE: 400,
        cv.ERROR: 'Bad Request'
    }


def main():
    """
    Загрузка параметров командной строки, если нет параметров, то задаём значения по умолчанию.
    Сначала обрабатываем порт:
    server.py -p 8888 -a 127.0.0.1
    :return:
    """

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = cv.DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('После параметра -\'p\' необходимо указать номер порта')
        sys.exit(1)
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535')
        sys.exit(1)

    # Затем загружаем какой адрес слушать
    try:
        listen_address = sys.argv[sys.argv.index('-a') + 1] if '-a' in sys.argv else ''
    except IndexError:
        print('После параметра -\'a\' необходимо указать адрес, который будет слушать сервер')
        sys.exit(1)

    # Готовим сокет
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.bind((listen_address, listen_port))

    # Слушаем порт
    transport.listen(cv.MAX_CONNECTIONS)

    while True:
        client, client_address = transport.accept()
        try:
            message_from_client = get_message(client)
            print(message_from_client)
            response = process_client_message(message_from_client)
            send_message(client_address, response)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Принято некорректное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
