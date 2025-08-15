# grades = input("Введите свои оценки через пробел: ").split()
# print(grades)
#
# for grade in grades:
#     if grade.isdigit():
#         grade = int(grade)
#         if grade == 5:
#             print("Отлично")
#         elif grade == 4:
#             print("Хорошо")
#         elif grade == 3:
#             print("Удовлетворительно")
#         elif grade == 2:
#             print("Плохо")
#         else:
#             print("Такой оценки нет")
#             break
#     else:
#         print('Введите оценку!')
from pygments.lexer import words

# my_list = ['orange', 'banana', 'apple']
# for i, value in enumerate(my_list):
#     print(i, value)


# BAD_LETTER = 'ш'
# MAX_COUNT_LETTER = 2
#
# words_letter = input('Введите слова для проверки. Слова должны быть введены через пробел.').split()
# print(f'Вот список слов, который у вас получился: {words_letter}')
#
# bad_words = []
# letter_count = 0
# for word in words_letter:
#     letter_count = word.count(BAD_LETTER)
#     if letter_count >= MAX_COUNT_LETTER:
#         print(f'Слово {word} плохое. Добавляю его в список плохих слов')
#         bad_words.append(word)
#
# if bad_words:
#     print(f'Список плохих слов: {bad_words}')
# else:
#     print('Плохих слов не было написано')
#



# shop_list = []
#
# max_count_tovar = input('Введите максимальное количество товаров, которое вы хотите положить в корзину:')
#
# if max_count_tovar.isdigit():
#     max_count_tovar = int(max_count_tovar)
#
# for i in range(max_count_tovar):
#     i += 1
#     tovar = input(f'Введите товар {i}:')
#     shop_list.append(tovar)
#
# print(f'Ваш список: {list(enumerate(shop_list, start=1))}')


#
# my_list_1 = ['1', '2', '3', '4']
#
# print(list(enumerate(my_list_1, start= 1 )))


#
# my_list_2 = input('Введите последовательность товаров на вывод через пробел: ').split()
#
# my_list_2 = list(enumerate(my_list_2, start=1))
# print(my_list_2)
#
# for i, product in my_list_2:
#     print(f'Товар с ключевым номером {i}: {product}')
