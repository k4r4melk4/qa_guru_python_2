from pprint import pprint
from marvel import full_dict as marvel_dict



# import marvel
#
# pprint(marvel.simple_set.copy())
# или
# from marvel import full_dict



# users_dict_1 = {}
#
# users_dict_1['name'] = 'Maks'
# users_dict_1['age'] = '30'
#
# users_dict_1.update(
#     {
#         'height': '197',
#         'is_student': True
#     }
# )
#
# pprint(users_dict_1)

#
# ad1 = {"breed": "Pеrsian",
#        "age": 2,
#        "price": 1000,
#        "description": "Adorable Persian kitten"}
#
# pprint(ad1)
#
# print(type(list(ad1.keys())))
# print(type(list(ad1.values())))
# print(type(list(ad1.items())))
#
# name = ad1['breed']
# age = ad1.get('age')

# fruits_cart = {"apple": 80, "orange": 150, "banana": 120}
#
# for keys, value in fruits_cart.items():
#     print(f'Элемент {keys} в закупочной цене будет равен {round(value*0.9, 1)}')


nested_dict = {
    'one': {'a': 1, 'b': 2},
    'two': {'c': 3, 'd': 4},
    'three': {'e': 5, 'f': 6}
}


# for key in marvel_dict.keys():
#     for nested_key in marvel_dict[key].keys():
#         print(key, nested_key)


# for value in nested_dict.values():
#     for nested_value in value.values():
#         print(value, nested_value)



for key, value in nested_dict.items():
    for nested_key, nested_value in value.items():
        print(f"{key}, {value} - данные первого словаря")
        print(f"{nested_key}, {nested_value} - данные вложенного словаря")

