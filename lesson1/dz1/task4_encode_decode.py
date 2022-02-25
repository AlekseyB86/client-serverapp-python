"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и
выполнить обратное преобразование (используя методы encode и decode).
"""
import locale


def get_byte(word_str):
    encoding_system = locale.getpreferredencoding()
    try:
        return word_str.encode(encoding_system)
    except Exception as e:
        print(f'Ошибка: {e}')


def get_str(word_bytes):
    encoding_system = locale.getpreferredencoding()
    try:
        return word_bytes.decode(encoding_system)
    except Exception as e:
        print(f'Ошибка: {e}')


def main():
    word = input('Введите слово: ')
    print(word, len(word), type(word))
    print(f'Кодировка системы: {locale.getpreferredencoding()}')

    print("====================Кодирование====================")
    word_bytes = get_byte(word)
    print(word_bytes, len(word_bytes), type(word_bytes))

    print("====================Декодирование====================")
    word_byte_str = get_str(word_bytes)
    print(word_byte_str, len(word_byte_str), type(word_byte_str))

    print(f'word == word_byte_str: {word == word_byte_str}')


if __name__ == "__main__":
    main()
