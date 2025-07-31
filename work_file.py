# text = 'Привет МИР!'
#
# byte_string = text.encode('utf-8')
# print(text)


# file = open('1.txt', 'a', encoding='utf-8')
#
# file.write('Третья запись' + '\n')
# file.close()
#
#
#
# # Контекстный менеджер
#
# text = ['Привет \n', 'Как дела? \n', 'Что делаешь ? \n']
#
#
# with open('2.txt', 'w', encoding='utf-8') as file:
#     for line in text:
#         file.write(line)

# чтение построчно
# with open('2.txt', 'r', encoding='utf-8') as file:
#     for line in file:
#         print(line.strip())


# чтение файла
# with open('2.txt', 'r', encoding='utf-8') as file:
#     print(file)
#     print(file.read())

# Чтение в список
# with open('2.txt', 'r', encoding = 'utf-8') as file:
#     print(file.readlines())
#     print(type(file.readlines()))