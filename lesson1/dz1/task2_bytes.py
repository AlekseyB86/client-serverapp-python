"""
Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя
методы encode, decode или функцию bytes) и определить тип, содержимое и длину  соответствующих переменных.
"""


def get_byte(letter):
    try:
        return eval(f'b"{letter}"')
    except SyntaxError as e:
        print(f'{letter}: не соотвествует ASCII!')


def main():
    letters = input('Введите что-нибудь: ')
    print(f'letters: {letters},  {type(letters)}, {len(letters)}')

    if letters_byte := get_byte(letters):
        print(f'letters_byte: {letters_byte}, {type(letters_byte)}, {len(letters_byte)}')
        print(f'letters == letters_byte: {letters == letters_byte}')


if __name__ == '__main__':
    main()
