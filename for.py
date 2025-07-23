# a = 1
#
# if a:
#     print ( ' Переменная не ноль')


# grade = int(input('введите'))
#
#
# if grade == 1:
#     print("1")
# else:
#     print('2')


# my_strin = 'Hello world!'
# for char in my_strin:
#     print(char, end='')

word_for_check = input("Введите слово для проверки: ")
counth = 0


for letter in word_for_check:
    if letter.lower() == 'ш':
        counth += 1
    if counth == 3:
        print(f'Не перегибай. Не буду читать {word_for_check}')
        break

else:
    print(f"Слово {word_for_check} хорошее, спасибо")

print(f"Слово {word_for_check} слишком трудное для прочтения, но я постараюсь")
