from os import write
from pprint import pprint
import csv
#
#
data_set = [
    ['Имя', 'Возраст', 'Группа'],
    ['Алексей', 21, 'БО-111111'],
    ['Анна', 20, 'БО-222222'],
    ['Александр', 19, 'БО-333333'],
    ['Антон', 20, 'БО-222222'],
    ['Андрей', 19, 'БО-333333'],
    ['Антонина', 20, 'БО-222222']
]


#newline = "" - убирает пустую строку между записями


# with open('new_csv.csv', 'w', encoding='windows-1251', newline='') as file:
#     writer = csv.writer(file, delimiter = ';')
#     writer.writerows(data_set)

# with open('new_csv.csv', 'r', encoding='windows-1251') as file:
#     reader = csv.reader(file, delimiter=';')
#     print(type(reader))
#     data_set = list(reader)
#     pprint(data_set)
#


# new_row = ['Мария', 20, 'БО-222222']
#
# with open('new_csv.csv', 'a', encoding='windows-1251') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow(new_row)



with open('new_csv.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    print(type(reader))
    data_set = list(reader)
    print(type(data_set))
    pprint(data_set)



new_row_1 = {
    'Имя': 'Анна',
    'Возраст': 22,
    'Группа': 'БО-222222'
}


with open('new_csv.csv', 'r', encoding='windows-1251', newline="") as file:
    fieldnames = ['Имя', 'Возраст', 'Группа']
    writer = csv.DictWriter(file, delimiter=';', fieldnames = fieldnames)
    print(type(reader))
    writer.writerows(new_row_1)