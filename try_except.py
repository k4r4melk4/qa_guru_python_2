int_a = input('Введите делимое:')
int_b = input('Введите делитель:')

try:
    int_a = int(int_a)
    int_b = int(int_b)
    result = int_a/int_b
except ValueError as qwe:
    print(f"Вы ввели не число {qwe}")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(f'Результат вычисления: {result}')
finally:
    print("Завершение программы")



student_mark = input('Введите (от 0 до 10):')

try:
    student_mark = int(student_mark)
except ValueError:
    print('Вы ввели не число')
else:
    if not (0 <= student_mark <= 10):
        raise ValueError('Вы не попали в диапазон')