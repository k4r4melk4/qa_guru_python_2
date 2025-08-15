THRESHOLD_DIGITS = 1
THRESHOLD_UPPER = 1
THRESHOLD_LOWER = 1
THRESHOLD_LEN = 8
# Cчетчики для проверки
digit_counter = 0
upper_counter = 0
lower_counter = 0
# принты для проверки пароля
# print(f"Пароль '{input_password}' надежный")
# print(f"Пароль '{input_password}' ненадежный")

input_password = input("Введите пароль: ")
for char in input_password:
    if char.isdigit():
        digit_counter += 1
    elif char.lower() == char:
        lower_counter += 1
    elif char.upper() == char:
        upper_counter += 1

if len(input_password) < THRESHOLD_LEN:
    print(f"Пароль '{input_password}' ненадежный")
elif digit_counter < THRESHOLD_DIGITS:
    print(f"Пароль '{input_password}' ненадежный")
elif upper_counter < THRESHOLD_UPPER:
    print(f"Пароль '{input_password}' ненадежный")
elif lower_counter < THRESHOLD_LOWER:
    print(f"Пароль '{input_password}' ненадежный")
else:
    print(f"Пароль '{input_password}' надежный")



