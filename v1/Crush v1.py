import hashlib
import random
import time
import os


def prob():  # Чистим консоль
    os.system('cls||clear')

def vivod():  # Красивый вывод с таймингами
    prob()
    if mas[i] < 2:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.05)
    elif mas[i] < 3:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.03)
    elif mas[i] < 5:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.02)
    elif mas[i] < 10:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.01)
    elif mas[i] < 20:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.005)
    else:
        print('╭─────ᘒ─────╮')
        print('    ', mas[i], '      ')
        print('╰─────ᘒ─────╯')
        time.sleep(.001)


crush = round(1 / random.random(), 2)  # Генерация рандомного краша
crush1 = int(crush * 100)
mas = []
salt = ''
ran = 'abcdefghijklmnopqrstuvwxyz1234567890'  # Строка с рандомными символами
for i in range(32):  # Генерируем salt
    salt = salt + ran[random.randint(0, 35)]
salt = str(crush) + '+' + salt
salt1 = hashlib.sha256(salt.encode('utf-8'))
hash1 = salt1.hexdigest()  # Соединяем с крашем и хешируем
for i in range(100, crush1 + 1):
    mas.append(i / 100)  # Заполняем масив от 1.00 до краша с шагом 0.01
print('Последние 5 крашей: ')
with open('log.txt') as f:  # Выводим последние 5 крашей
    text = f.readlines()
print(text[len(text) - 1])
for i in range(len(text) - 2, len(text) - 6, -1):
    print(text[i], end='')
# print("lines number:", len(text)) # Закомментированый
f.close()
print('Проверка на честность. HASH =', hash1)  # Выведем HASH
st = float(input('Сумма вашей ставки: '))  # И спросим ставку когда все сгенерировано
kf = float(input('Коэффицент: '))
for i in range(len(mas)):  # Покрутили цифры)
    vivod()
prob()
if kf <= mas[len(mas) - 1]:  # Выводим проеб или нет
    print('CRUSH', mas[len(mas) - 1])
    print('Ваш выигрыш:', round(kf * st, 2))
    print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный HASH')
    print(salt)
    print('HASH =', hash1)
else:
    print('CRUSH', mas[len(mas) - 1])
    print('Ваш выигрыш: 0')
    print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный HASH')
    print(salt)
    print('HASH =', hash1)
f = open('log.txt', 'a')
f.write(f"\n{crush}")  # Заносим краш в историю
f.close()
x = input('Для продолжения перезапустите приложение')
