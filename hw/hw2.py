# Секретное послание
secret_letter = [['DFВsjl24sfFFяВАДОd24fssflj234'], ['asdfFп234рFFdо24с$#afdFFтasfо'],
['оafбasdf%^о^FFжа$#af243ю'],['afпFsfайFтFsfо13н'],
['fн13Fа1234де123юsdсsfь'], ['чFFтF#Fsfsdf$$о'],
['и$ sfF'], ['вSFSDам'],['пSFоsfнрSDFаSFвSDF$иFFтsfaсSFя'],
['FFэasdfтDFsfоasdfFт'], ['FяDSFзFFsыSfкFFf']]
# Список с маленькими русскими буквами
small_rus = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н',
             'о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
# Вот что у меня получилось
# ВВЕДИТЕ ТУТ ВАШ КОД

decrypted_word = []

for list in secret_letter:
    list_join = "".join(list)
    for i in list_join:
        if i.lower() in small_rus and i.lower() == i:
            decrypted_word.append(i)
    decrypted_word.append(' ')
decrypted_letter = ''.join(decrypted_word)
print(decrypted_letter.capitalize())
"""
Введите то, что вы получили в терминале, в результате расшифровки
"""

