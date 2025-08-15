# my_set_1 = {1, 2, 3}
#
# my_set_1.remove(4)
# # my_set_1.discard(4)
#
# my_set_2 = set()
# for i in range(1,10000):
#     my_set_2.add(i)
# print(my_set_2)
#
# my_set_2 = { 'Oleg', 'Maks', 'Ilya', 'Anna', 'Oleg', 'Maks', 'Ilya'}
#
# while my_set_2:
#     elem = my_set_2.pop()
#     print(elem)


pokemons_alice = {'Пикачу', 'Иви', 'Бульбазавр', 'Чаризард', 'Сквиртл'}
pokemons_nikita = {'Варортл', 'Метапод', 'Амбреон', 'Пикачу', 'Пиджи'}

print(f'Общая коллекция: {pokemons_nikita.intersection(pokemons_alice)}')

print(f'Есть только у Никиты: {pokemons_nikita - pokemons_alice}')

print(f'Есть только у Алисы: {pokemons_alice - pokemons_nikita}')

print(f'Есть у Алисы/Никиты, но нет у обоих: {pokemons_nikita.symmetric_difference(pokemons_alice)}')

