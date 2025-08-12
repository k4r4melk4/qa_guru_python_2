from cities import cities
from pprint import pprint

collections_cities = {city['name'].lower() for city in cities}
result_list = []
count_iteration = 0
list_error_letter = ["ь", "ъ"]
list_replace_letter = ["ё", "й"]
word_pc = ''

def is_exit_in_game(input_user: str) -> bool:
    """
    :param input_user:
    :return: Проверяет введенное пользователем значение на "Стоп"
    Если введенное пользователем значение == "стоп" - осуществляется выход из игры
    """
    return input_user.lower().strip() == 'стоп'


def is_city_user_in_set(input_user: str,set_cities: set) -> bool:
    """
    :param input_user: - пользовательский ввод
    :param set_cities: - список всех городов
    :return: Функция должна вернуть ответ:
    входит ли город пользователя в список городов
    """
    return input_user.lower().strip() in set_cities


def response_pc_last_letter(input_user: str,set_cities: set) -> str:
    """
    :param input_user: - город, названный пользователем
    :param set_cities: - список всех городов
    :return: Функция должна вернуть город,
    заканчивающийся на последнюю букву города, названного пользователем
    """
    global word_pc
    for i in set_cities:
        if i[0:1] == input_user[-1:]:
            word_pc = i
            print(f'Ответ ПК: {word_pc}')
            break
    return word_pc


def response_pc_second_to_last_letter(input_user: str,set_cities: set) -> str:
    """
    :param input_user: - город, названный пользователем
    :param set_cities: - список всех городов
    :return: Функция должна вернуть город,
    заканчивающийся на предпоследнюю букву города, названного пользователем
    """
    global word_pc
    for i in set_cities:
        if i[0:1].lower() == input_user[-2:-1].lower():
            word_pc = i
            print(f'Ответ ПК: {word_pc}')
            break
    return word_pc


def is_last_letter_user_in_error_list(input_user: str, error_list: list[str]) -> bool:
    """
    :param input_user: Последняя буква слова, введенного пользователем
    :param error_list: Список запрещенных букв
    :return: Функция должна вернуть результат вхождения последней буквы слова пользователя
    в список запрещенных букв
    """
    return input_user[-1:] in error_list


def is_last_letter_pc_in_error_list(output_pc: str, error_list: list[str]) -> bool:
    """
    :param output_pc: Последняя буква слова, введенного ПК
    :param error_list: Список запрещенных букв
    :return: Функция должна вернуть результат вхождения последней буквы слова ПК
    в список запрещенных букв
    """
    return output_pc[-1:] in error_list


def is_replace_second_to_last_user(input_user: str, replace_list: list[str]) -> bool:
    """
    :param input_user: Последняя буква слова, введенного пользователем
    :param replace_list: Список запрещенных букв
    :return: Функция должна вернуть результат вхождения предпоследней буквы слова пользователя
    в список запрещенных букв
    """
    return input_user[-2:-1] in replace_list


def is_replace_second_to_last_pc(output_pc: str, replace_list: list[str]) -> bool:
    """
    :param output_pc: Последняя буква слова, введенного ПК
    :param replace_list: Список запрещенных букв
    :return: Функция должна вернуть результат вхождения предпоследней буквы слова ПК
    в список запрещенных букв
    """
    return output_pc[-2:-1] in replace_list


def replace_second_to_last_letter_pc(output_pc: str) -> str:
    """
    :param output_pc: Предпоследняя буква слова, которым ответил ПК
    :return: Функция должна вернуть замену на другую букву , если предпоследняя буква слова,
    введенного ПК, входит в список букв под замену
    """
    if output_pc[-2:-1].lower() == 'ё':
        output_pc = output_pc[-2:-1].replace('ё', 'е')
    elif output_pc[-2:-1].lower() == 'й':
        output_pc = output_pc[-2:-1].replace('й', 'и')
    return output_pc
def replace_second_to_last_letter_user(input_user: str) -> str:
    """
    :param input_user: Предпоследняя буква слова, которым ответил пользователь
    :return: Функция должна вернуть замену на другую букву, если предпоследняя буква слова,
    введенного пользователем, входит в список букв под замену
    """
    if input_user[-2:-1].lower() == 'ё':
        input_user[-2:-1].replace('ё', 'е')
    elif input_user[-2:-1].lower() == 'й':
        input_user[-2:-1].replace('й', 'и')
    return input_user

def is_check_last_letter(input_user: str, output_pc: str) -> bool:
    """
    :param input_user: -  ввод пользователя
    :param output_pc: - ответ пк
    :return: Функция проверяет правильно ли пользователь ответил на последнюю букву слова ПК
    """
    return input_user[1:2] == output_pc[-1:]

def is_check_second_to_last_letter(input_user: str, output_pc: str) -> bool:
    """
    :param input_user: - ввод пользователя
    :param output_pc: - ответ пк
    :return: Функция проверяет правильно ли пользователь ответил на предпоследнюю букву слова ПК
    """
    return input_user[1:2] == output_pc[-2:-1]


def main():
    global count_iteration
    global word_pc
    while collections_cities:
        input_user = input('Введите название города или "Стоп" для завершения игры:').lower()
        if is_exit_in_game(input_user):
            print("Выход из игры..")
            break
        # проверка на вхождение слова пользователя в set
        elif is_city_user_in_set(input_user, collections_cities):
            collections_cities.remove(input_user)
            # если итераций больше 1
            if count_iteration >= 1:
                # проверка на вхождение последней буквы слова пк в error_list
                if is_last_letter_pc_in_error_list(word_pc, list_error_letter):
                    # проверка на вхождение предпоследней буквы в replace_list
                    if is_replace_second_to_last_pc(word_pc,list_replace_letter):
                        # замена предпоследней буквы на аналог
                        word_pc = replace_second_to_last_letter_pc(word_pc)
                        # проверка правильно ли пользователь ответил на слово ПК
                        if is_check_second_to_last_letter(input_user,word_pc):
                            continue
                        else:
                            print('Неправильный ответ')
                            break
                    else:
                        if is_check_second_to_last_letter(input_user, word_pc):
                            continue
                        else:
                            print('Неправильный ответ')
                            break
                else:
                    if is_check_last_letter(input_user, word_pc):
                        continue
                    else:
                        print('Неправильный ответ')
                        break

            # проверка на вхождение последней буквы в error_list
            if is_last_letter_user_in_error_list(input_user, list_error_letter):
                # проверка на вхождение предпоследней буквы в replace_list
                if is_replace_second_to_last_user(input_user, list_replace_letter):
                    # замена предпоследней буквы на аналог
                    input_user = replace_second_to_last_letter_user(input_user)
                    word_pc = response_pc_second_to_last_letter(input_user, collections_cities)
                # если нет, то компьютер отвечает согласно предпоследней букве
                else:
                    word_pc = response_pc_second_to_last_letter(input_user, collections_cities)
            # если нет, то компьютер отвечает согласно последней букве
            else:
                response_pc_last_letter(input_user, collections_cities)
        else:
            print('Такого слова нет в списке городов')
            break

    count_iteration += 1

main()