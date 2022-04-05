from subprocess import Popen, CREATE_NEW_CONSOLE
import time

process_list = []
cnt_users = 5
while True:
    user_command = input("Запустить несколько клиентов (s) / Закрыть всех клиентов (x) / Выйти (q) ")

    if user_command == 'q':
        break
    elif user_command == 's':
        process_list.append(
            Popen('python server.py', creationflags=CREATE_NEW_CONSOLE)
        )

        time.sleep(2)
        process_list.extend(
            Popen(
                f'python -i client.py -a localhost -p 7777 -u user{num}',
                creationflags=CREATE_NEW_CONSOLE,
            )
            for num in range(1, cnt_users + 1)
        )

        print(f'Запущено {cnt_users} клиентов и сервер')
    elif user_command == 'x':
        for p in process_list:
            p.kill()
        process_list.clear()
