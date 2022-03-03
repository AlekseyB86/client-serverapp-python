"""Программа-клиент"""

import sys
import json
import socket
import time
import common.variables as cv
from common.utils import get_message, send_message


def create_presence(account_name='Guest'):
    """
    Функция генерирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    return {
        cv.ACTION: cv.PRESENCE,
        cv.TIME: time.time(),
        cv.USER: {
            cv.ACCOUNT_NAME: account_name
        }
    }


def process_ans(message):
    """
    Функция разбирает ответ сервера
    :param message:
    :return:
    """
    if cv.RESPONSE in message:
        return '200 : OK' if message[cv.RESPONSE] == 200 else f'400 : {message[cv.ERROR]}'
    raise ValueError


def main():
    """Загружаем параметы коммандной строки"""
    try:
        server_address = sys.argv[1]
        server_port = int(sys.argv[2])
        if server_port < 1024 or server_port > 65535:
            raise ValueError
    except IndexError:
        server_address = cv.DEFAULT_IP_ADDRESS
        server_port = cv.DEFAULT_PORT
    except ValueError:
        print('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')
        sys.exit(1)

    # Инициализация сокета и обмен
    transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    transport.connect((server_address, server_port))
    message_to_server = create_presence()
    send_message(transport, message_to_server)
    try:
        answer = process_ans(get_message(transport))
        print(answer)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
