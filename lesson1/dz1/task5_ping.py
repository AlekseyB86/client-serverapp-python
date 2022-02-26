"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать
 результаты из байтовового в строковый тип на кириллице.
"""
import locale

import chardet  # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform


def ping_ip(site):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    args = ['ping', param, '3', site]
    process = subprocess.Popen(args, stdout=subprocess.PIPE)
    system_encoding = locale.getpreferredencoding()
    for line in process.stdout:
        result = chardet.detect(line)
        print('result = ', result)
        line = line.decode(result['encoding']).encode(system_encoding)
        print(line.decode(system_encoding))


def main():
    site_ip = input('Какой сайт/IP будем пинговать: ')
    ping_ip(site_ip)


if __name__ == '__main__':
    main()
