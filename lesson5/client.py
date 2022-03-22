"""Программа Клиент"""
import sys
import json
import time
import socket
from config import *


def create_presence_message(account_name='Guest'):
    if len(account_name) > 25:
        raise ValueError

    if not isinstance(account_name, str):
        raise TypeError

    return {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }


def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if server_address != '0.0.0.0':
        s.connect((server_address, server_port))
    else:
        s.connect(('localhost', server_port))

    message = create_presence_message()
    if isinstance(message, dict):
        # Преобразование объекта Python в строку JSON
        message = json.dumps(message)
    print(f'Отправляю сообщение "{message}" на сервер', end=' ')

    # Кодируем строку в байты, используя кодировку utf-8
    s.send(message.encode('utf-8'))
    print('жду ответа')

    # Раскодирование байтстроки в строку, используя кодировку utf-8
    # Преобразование строки JSON в объекты Python
    server_response = json.loads(s.recv(1024).decode('utf-8'))
    print('Ответ:', server_response)
    if server_response.get('response') not in StandartServerCodes:
        s.close()
        raise UnknownCode(server_response.get('response'))
    if server_response.get('response') == OK:
        print('Сервер нас понимает!')
    else:
        print('Что-то пошло не так..')
    s.close()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        server_address = sys.argv[1]
    if len(sys.argv) > 2:
        try:
            server_port = int(sys.argv[2])
        except ValueError:
            'Порт должен быть целым числом!'
    start_client()
