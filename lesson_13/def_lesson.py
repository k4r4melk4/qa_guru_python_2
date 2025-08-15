#
#
# def examination_password(password):
#     if len(password) < 10:
#         return False
#     else:
#         return True
#
# input_password = input('Введите пароль: ')
#
# if examination_password(input_password):
#     print('Гуд')
# else:
#     print('Нот гуд')
#
# def greeting_user(name, age = 18):
#     '''
#
#     :param name: Имя человека
#     :param age: Возраст человека
#     :return:
#     '''
#     print(f'Hello, {name}! You are {age} years old.')
# #
# # def greeting_user2(name, age ):
# #     print(f'Hello, {name}! You are {age} years old.')
# #
# greeting_user('Alice')
# greeting_user('John', 19)
#
#
# greeting_user2(age = 10, name = 'Maks')



# def get_sum(int1, int2):
#     return int1 + int2
#
# print(get_sum(12, 13))

# some_list = [1,2,3,4,5]

# print(*some_list)
#
#
# def get_sum(*args):
#     # print(args)
#     return sum(args)
#
# print(get_sum(1,2,3,4,5,5,56,6,6))
#
#
# int_list = input('Введите числа для сложения: ').split()
#
#
# int_list =[int(i) for i in int_list if i.isdigit()]
# # for chislo in int_list:
# #     if chislo.isdigit():
# #         chislo = int(chislo)
# #         new_int_list.append(chislo)
#
# print(get_sum(*int_list))



# some_dict = { 'sep': '11' }
#
#
#
# def get_dict_print(dictionary):
#     print(**dictionary)
#
# get_dict_print(some_dict)



## Области видимости переменных

# 1/Встроенная
# 2/Глобальная
# 3/Локальная области видимости
# x = 'привет'

# def foo():
#     global x
#     x = x * 2
#     print(x)
#
# foo()


# def outer():
#     a = 1
#     print(f'outer: {a}')
#     def inner():
#         # nonlocal a
#         a = 2
#         print(f'outer: {a}')
#     inner()
#     print(f'outer: {a}')
#
# outer()

name_for_search = 'Andry'

names = ['Alice', 'John', 'Maks', 'Liya', 'Alex', 'Andry', 'Oleg', 'Andry']

# def search_name(list):
#
#     name_lst = []
#     for key, value in enumerate(list, start=1):
#         if value == name_for_search:
#             name_lst.append(key)
#     return name_lst
#
# print(search_name(names))



# def return_random_names(list):
#     list = set(list)
#     name_1 = list.pop()
#     name_2 = list.pop()
#     name_3 = list.pop()
#     return name_1, name_2, name_3
#
# print(return_random_names(names))



def fun_sum(a: int, b: int) -> int:
    return a+b

fun_sum(2,  44)