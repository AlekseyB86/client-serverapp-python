"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode
и также проверить тип и содержимое переменных.
онлайн-конвертор текста в unicode: https://calcsbox.com/post/konverter-teksta-v-unikod.html
"""

# word_1_str = 'разработка'
# word_2_str = 'сокет'
# word_3_str = 'декоратор'
# print(f'word_1_str: {word_1_str} - {type(word_1_str)}')
# print(f'word_2_str: {word_2_str} - {type(word_2_str)}')
# print(f'word_3_str: {word_3_str} - {type(word_3_str)}')
#
# word_1_unicode = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
# word_2_unicode = '\u0441\u043e\u043a\u0435\u0442'
# word_3_unicode = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'
# print(f'word_1_unicode: {word_1_unicode} - {type(word_1_unicode)}')
# print(f'word_2_unicode: {word_2_unicode} - {type(word_2_unicode)}')
# print(f'word_3_unicode: {word_3_unicode} - {type(word_3_unicode)}')
#
# print(f'word_1_str == word_1_unicode: {word_1_str == word_1_unicode}')
# print(f'word_2_str == word_2_unicode: {word_2_str == word_2_unicode}')
# print(f'word_3_str == word_3_unicode: {word_3_str == word_3_unicode}')

words = [
    ['разработка', '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'],
    ['сокет', '\u0441\u043e\u043a\u0435\u0442'],
    ['декоратор', '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
]

for item in words:
    print(f'word: {item[0]} / {item[1]} -> {type(item[0])} / {type(item[1])}, {item[0] == item[1]}')

