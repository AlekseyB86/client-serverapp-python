"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
 Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной
  кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
"""

from chardet import detect


def main():
    # запись в файл 3х строк
    str_1 = 'сетевое программирование'
    str_2 = 'sockеt'
    str_3 = 'декоратор'

    with open('test.txt', 'w', encoding='utf-8') as f:
        f.write(f'{str_1}\n'
                f'{str_2}\n'
                f'{str_3}')

    # определяем кодировку файла
    try:
        with open('test.txt', 'rb') as f:
            content = f.read()
        encoding = detect(content)['encoding']
        print('encoding: ', encoding)

        # читаем файл
        with open('test.txt', encoding=encoding) as f_n:
            for el_str in f_n:
                print(el_str, end='')
            print()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
