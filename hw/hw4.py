from cities.cities import cities
from pprint import pprint

set_cities = {city['name'].lower() for city in cities }
pprint(set_cities)
count_iteration = 0
list_error_letter = ["ё", "ь", "ъ"]
letter_pc = ''
while set_cities:
    input_user = input('Введите название города (или "Стоп" для завершения игры):').lower()
    if input_user == 'стоп':
        print('Выход из игры...')
        break
    if input_user in set_cities:
        set_cities.remove(input_user)
    else:
        print('Вы проиграли')
        break

    if count_iteration >= 1:
        if letter_pc[-1] in list_error_letter:
            if letter_pc[-2] == input_user[0]:
                break
            else:
                print('Слово не подходит')
        else:
            if letter_pc[-1:] == input_user[0:1]:
                break
            else:
                print('Слово не подходит')

    for i in set_cities:
        if i[0] == input_user[-1]:
            letter_pc = i
            set_cities.remove(i)
            print(i)
            break
    else:
        print("да ну нет")

    count_iteration += 1
    print(set_cities)