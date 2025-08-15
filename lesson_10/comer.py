from lesson_9.marvel import full_dict
from pprint import pprint
# names = ['Eve', 'Mallory', 'Oliver', 'Emily', 'Eve', 'Mallory', 'Oliver']
#
# name_start_e_1 = []
#
# for name in names:
#     if name.startswith('E') : # and name.endswith('e')
#         name_start_e_1.append(name)
# print(name_start_e_1)
#
# name_start_e_2 = [name.upper()
#                   for name in names
#                   if name.lower().startswith('o')]
#
# name_in_list_more_2 = [name for name in names if names.count(name) >= 1]
#
# name_in_list_more_2 = set(name_in_list_more_2)
# print(name_start_e_2)
# print(name_in_list_more_2)


# guests = {
#     "John Smith",
#     "Jane Smith",
#     "Alex Johnson",
#     "Alice Johnson",
#     "Jane Doe",
#     "John Doe",
#     "Jenny Doe",
#     "Alice Bell"
# }
#
#
# result = { guest for guest in guests if [name.split()[1] for name in guests].count(guest.split()[1]) > 1}
# print(result)



party_guests = {
    "Alice": 1,
    "Bob": 2,
    "Charlie": 3,
    "David": 1,
    "Eva": 2,
    "Fiona": 1
}

copied_party_guests = {}

# for guest, namber in party_guests.items():
#     copied_party_guests[guest] = namber


# copied_party_guests = {guest: namber for guest, namber in party_guests.items()}



# copied_party_guests = {guest: namber for guest, namber in party_guests.items() if namber > 1}
#
# print(copied_party_guests)



# film_from_2008 = {film: year for film, year in small_dict.items() if type(year) == int and year >= 2024}
#
# pprint(film_from_2008)

result = {film: stage for film, stage in full_dict.items() if stage['year'] == 2008}
pprint(result)