import json
from pprint import pprint
JSON_STRING = '''[
    {
        "name": "Alice",
        "age": 20,
        "grades": [88, 76, 92]
    },
    {
        "name": "Боб>",
        "age": 22,
        "grades": [81, 90, 95]
    },
    {
        "name": "Cathy",
        "age": 19,
        "grades": [80, 85, 83],
        "is_student": true
    }
]'''


#
# print(f'{type(JSON_STRING) = }')
#
#
#
# students_1 = json.loads(JSON_STRING)
# print(f'{type(students_1) = }')
# pprint(students_1)
# #
# #
# #
# # students_2 = json.dumps(students_1)
# # print(f'{type(students_2) = }')
#
# students_1.append(
#     {
#         "name": "Maks",
#         "age": 22,
#         "grades": [81, 90, 95]
#     }
# )
#
# print(students_1)
#
# with open('students.json', 'w', encoding='utf-8') as file:
#     json.dump(students_1, file, ensure_ascii=False, indent=3)

with open('students.json', 'r', encoding='utf-8') as file:
    students_list = json.load(file)


# pprint(students_list)


students_more_21 = [students for students in students_list if students['age'] >= 21]
pprint(students_more_21)