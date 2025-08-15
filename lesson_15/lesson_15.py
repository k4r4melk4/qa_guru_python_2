# #lambda function
# add = lambda x,y: x + y
#
# #map function
#
# numb_input = input('Введите последовательность чисел: ').split()
#
# # nums = list(map(int, numb_input))
# # nums = list(map(lambda x: int(x) if x.isdigit() else None, numb_input))
#
# nums = [int(x) if x.isdigit() else None for x in numb_input]
#
# print(nums)

#filter function

# nums = list(filter(lambda x: x.isdigit, numb_input))

# movies_2008 = dict(filter(lambda x: x[1]['year'] == 2010, full_dict.items()))
#
# pprint(movies_2008)


fruits = ["banana", "apple", "kiwi", "grape"]

# fruits.sort()
# print(fruits)
#
# fruits.sort(reverse=True)
# print(fruits)
#
# fruits.sort(key=len)
# print(fruits)
#
# fruits.sort(key=lambda x: x[::-1])
# print(fruits)
#
# fruits.sort(key=lambda x: x.count('a') >=2)
# print(fruits)


# person_dict = {
#     'age': 30,
#     'books': ['book1', 'book2', 'book3'],
#     'car': 'Ford',
#     'city': 'New York',
#     'name': 'John'
# }
#
# sorted_dict = dict(sorted(person_dict.items()))
# print(sorted_dict)
#
# sorted_dict = dict(sorted(person_dict.items(), key = lambda x: x[0][1]))
# print(sorted_dict)


# sorted_marvel_1 = dict(sorted(full_dict.items(), key=lambda x: x[1]['year'] == 2008 if type(x[1]['year'] == 2008) == int else  3000))
# print(sorted_marvel_1)
#
#
# sorted_marvel = dict(sorted(full_dict.items(), key=lambda x: x[1]['title']))
# print(sorted_marvel)
#
# list_1 = [1, 0, 0]
# print(any(i != 1 for i in list_1))
#
# list_2 = [1, 1, 1]
# print(all(i == 1 for i in list_2))



# input_str = input('Введите стрку для проверки: ').split()

# input_str = 'dfsd fsdgs  fgf'.split()


# for item in input_str:
#     if item == '':
#         input_str.pop()
#
# print(input_str)
# result = all(x.isdigit() for x in input_str)
#
# if result:
#     print('Вы ввели строку полностью состоящую из чисел')
# else:
#     print('Вы ввели строку содержашую как числа, так и буквы ')


matrix = [
    [6, 4 , 5],
    [3, 4 , 5],
    [5, 7 , 9],
]

two_in_matrix_1 = any(4 in row for row in matrix)
print(two_in_matrix_1)

two_in_matrix_1 = any(map(lambda x: 4 in x, matrix))


all_nums = all([all([isinstance(item, int) for item in row]) for row in matrix])
