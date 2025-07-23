# fruits = ['apple', 'banana', 'cherry']
#
#
# while True:
#
#     for fruit in fruits:
#         for letter in fruit.lower():
#             if letter == 'n':
#                 print(letter)
#                 print(f"Перебор слова {fruit} остановлен. Содержится недопустимая буква {letter}")
#                 print()
#                 break
#             print(letter)
#         else:
#             print(f"Перебор слова {fruit} завершен ")
#             print()
#     else:
#         print(f"Перебор списка завершен ")
#
#     while True:
#         ask = input('Хотите повторить разбор (y/n)?')
#
#         if ask.isdigit() and ask == 'n':
#             print("Спасибо")
#             break
#         else:
#             print('Введите букву: y - для продолжения , n - для завершения программы')



first_list_word = input('Введите список слов для проверки на слова-палиндромы.'
                        'Ввод осуществить через пробел'
                        'Если хотите выйти из программы - введите "Стоп": ').lower().split()


edit_list_word = []

if 'стоп' in first_list_word[0]:
    print('Выход...')
else:
    for word in first_list_word:
        if word == word[::-1]:
            print(f'Слово {word} палиндром')
            edit_list_word.append(word)
        else:
            print(f'Слово {word} не является палиндромом')
    if edit_list_word:
        print(f'Список слов палиндромов:'
              f'{",".join(edit_list_word)}.')
    else:
        print('Список пуст. Вы не ввели ни одного слова-палиндром')