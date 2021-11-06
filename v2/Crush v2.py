import hashlib
import os
import random
import time
import colorama
from colorama import Fore, Back


def prob():  # Чистим консоль
    os.system('cls||clear')


try:
    colorama.init()
    print(Fore.LIGHTGREEN_EX + 'Приветствую вас в миниигре Crush by BlackAlex\n'
                               'Правила весьма просты, вы вводите ставку и коэффицент, если коэффицент, на котором '
                               'оборвется игра (Crush) '
                               'будет не меньше вашего, то ваша ставка приумножается на коэффицент')
    sum1 = float(input('Введите начальную сумму (баланс): '))
    sum2 = sum1
    os.system('cls||clear')
    x = 'да'
    while x.lower() == 'да' or x.lower() == 'yes' or x.lower() == 'y' or x.lower() == 'д' or x.lower() == 'lf':
        print(Fore.RESET, end='')
        crush = round(1 / random.random(), 2)  # Генерация рандомного краша
        crush1 = int(crush * 100)
        mas = []
        salt = ''
        ran = str('abcdefghijklmnopqrstuvwxyz1234567890')  # Строка с рандомными символами
        for i in range(32):  # Генерируем salt
            salt = salt + ran[random.randint(0, 35)]
        salt = str(crush) + '+' + salt
        salt1 = hashlib.sha256(salt.encode('utf-8'))
        hash1 = salt1.hexdigest()  # Соединяем с крашем и хешируем
        for i in range(100, crush1 + 1):
            mas.append(i / 100)  # Заполняем масив от 1.00 до краша с шагом 0.01
        with open('log.txt') as faille:  # Выводим последние 5 крашей
            text = faille.readlines()
        print('Последние 5 крашей: ')
        if float(text[len(text) - 1]) < 1.2:
            print(Fore.RED + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 2:
            print(Fore.BLUE + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 3:
            print(Fore.GREEN + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 5:
            print(Fore.MAGENTA + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 10:
            print(Fore.LIGHTMAGENTA_EX + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 20:
            print(Fore.YELLOW + text[len(text) - 1])
        else:
            print(Fore.YELLOW + text[len(text) - 1])
        for i in range(len(text) - 2, len(text) - 6, -1):
            if float(text[i]) < 1.2:
                print(Fore.RED + text[i], end='')
            elif float(text[i]) < 2:
                print(Fore.BLUE + text[i], end='')
            elif float(text[i]) < 3:
                print(Fore.GREEN + text[i], end='')
            elif float(text[i]) < 5:
                print(Fore.MAGENTA + text[i], end='')
            elif float(text[i]) < 10:
                print(Fore.LIGHTMAGENTA_EX + text[i], end='')
            elif float(text[i]) < 20:
                print(Fore.YELLOW + text[i], end='')
            else:
                print(Fore.YELLOW + text[i], end='')
        # print("lines number:", len(text)) # Закомментированый
        faille.close()
        print(Fore.GREEN + 'Проверка на честность. HASH =', hash1)  # Выведем HASH
        st = float(input(Fore.YELLOW + 'Сумма вашей ставки: '))  # И спросим ставку когда все сгенерировано
        while sum1 - st < 0:
            prob()
            st = float(input(Fore.YELLOW + 'Сумма вашей КОРРЕКТНОЙ ставки: '))
        sum1 -= st
        kf = float(input('Коэффицент: '))
        for i in range(len(mas)):  # Покрутили цифры)
            prob()
            if mas[i] < 1.2:
                print(Fore.RED + '╭─────ᘒ─────╮')
                print(Fore.RED + '    ', mas[i], '      ')
                print(Fore.RED + '╰─────ᘒ─────╯')
                time.sleep(.05)
            elif mas[i] < 2:
                print(Fore.BLUE + '╭─────ᘒ─────╮')
                print(Fore.BLUE + '    ', mas[i], '      ')
                print(Fore.BLUE + '╰─────ᘒ─────╯')
                time.sleep(.05)
            elif mas[i] < 3:
                print(Fore.GREEN + '╭─────ᘒ─────╮')
                print(Fore.GREEN + '    ', mas[i], '      ')
                print(Fore.GREEN + '╰─────ᘒ─────╯')
                time.sleep(.03)
            elif mas[i] < 5:
                print(Fore.MAGENTA + '╭─────ᘒ─────╮')
                print(Fore.MAGENTA + '    ', mas[i], '      ')
                print(Fore.MAGENTA + '╰─────ᘒ─────╯')
                time.sleep(.02)
            elif mas[i] < 10:
                print(Fore.LIGHTMAGENTA_EX + '╭─────ᘒ─────╮')
                print(Fore.LIGHTMAGENTA_EX + '    ', mas[i], '      ')
                print(Fore.LIGHTMAGENTA_EX + '╰─────ᘒ─────╯')
                time.sleep(.01)
            elif mas[i] < 20:
                print(Fore.YELLOW + '╭─────ᘒ─────╮')
                print(Fore.YELLOW + '    ', mas[i], '      ')
                print(Fore.YELLOW + '╰─────ᘒ─────╯')
                time.sleep(.005)
            else:
                print(Fore.YELLOW + '╭─────ᘒ─────╮')
                print(Fore.YELLOW + '    ', mas[i], '      ')
                print(Fore.YELLOW + '╰─────ᘒ─────╯')
                time.sleep(.001)
        prob()
        if kf <= mas[len(mas) - 1]:  # Выводим проигрыш или нет
            print(Fore.GREEN + 'CRUSH', mas[len(mas) - 1])
            print('Ваш выигрыш:', round(kf * st, 2))
            sum1 += round(kf * st, 2)
            print('Ваш баланс -', sum1)
            if input('Хотите проверить ставку на честность? (Да/нет)').lower() == 'да':
                print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный '
                      'HASH')
                print(salt)
                print('HASH =', hash1)
        else:
            print(Fore.RED + 'CRUSH', mas[len(mas) - 1])
            print('Ваш выигрыш: 0')
            print('Ваш баланс -', sum1)
            if input(Fore.RESET + 'Хотите проверить ставку на честность? (Да/нет)').lower() == 'да':
                print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный '
                      'HASH')
                print(salt)
                print('HASH =', hash1)
        if sum1 == 0:
            print(Fore.RED + 'Вы проиграли)))')
            print('Спасибо за игру в Crush Simulator by BlackAlex')
            x = input()
            break
        else:
            faille = open('log.txt', 'a')
            faille.write(f"\n{crush}")  # Заносим краш в историю
            faille.close()
            x = input(Fore.GREEN + 'Хотите продолжить? (Да/нет)')
    else:
        print(Fore.GREEN + 'Ваш баланс -', sum1)
        if round(sum1 / sum2) >= 1:
            print('Ваша начальная сумма приумножилась в', round(sum1 / sum2, 2), 'раз(а)')
        else:
            print(Fore.RED + 'Ваша начальная сумма уменьшилась в', round(sum1 / sum2, 2), 'раз(а)')
        print('Спасибо за игру в Crush Simulator by BlackAlex')
        x = input()
except FileNotFoundError:  # Создадим файл
    f = open('log.txt', 'w')
    f.write(str(round(1 / random.random(), 2)))
    for j in range(4):
        test = round(1 / random.random(), 2)
        f.write(f"\n{test}")
    f.close()
    x = 'да'
    while x.lower() == 'да' or x.lower() == 'yes' or x.lower() == 'y' or x.lower() == 'д' or x.lower() == 'lf':
        print(Fore.RESET + '')
        crush = round(1 / random.random(), 2)  # Генерация рандомного краша
        crush1 = int(crush * 100)
        mas = []
        salt = ''
        ran = str('abcdefghijklmnopqrstuvwxyz1234567890')  # Строка с рандомными символами
        for i in range(32):  # Генерируем salt
            salt = salt + ran[random.randint(0, 35)]
        salt = str(crush) + '+' + salt
        salt1 = hashlib.sha256(salt.encode('utf-8'))
        hash1 = salt1.hexdigest()  # Соединяем с крашем и хешируем
        for i in range(100, crush1 + 1):
            mas.append(i / 100)  # Заполняем масив от 1.00 до краша с шагом 0.01
        with open('log.txt') as faille:  # Выводим последние 5 крашей
            text = faille.readlines()
        print('Последние 5 крашей: ')
        if float(text[len(text) - 1]) < 1.2:
            print(Fore.RED + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 2:
            print(Fore.BLUE + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 3:
            print(Fore.GREEN + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 5:
            print(Fore.MAGENTA + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 10:
            print(Fore.LIGHTMAGENTA_EX + text[len(text) - 1])
        elif float(text[len(text) - 1]) < 20:
            print(Fore.YELLOW + text[len(text) - 1])
        else:
            print(Fore.YELLOW + text[len(text) - 1])
        for i in range(len(text) - 2, len(text) - 6, -1):
            if float(text[i]) < 1.2:
                print(Fore.RED + text[i], end='')
            elif float(text[i]) < 2:
                print(Fore.BLUE + text[i], end='')
            elif float(text[i]) < 3:
                print(Fore.GREEN + text[i], end='')
            elif float(text[i]) < 5:
                print(Fore.MAGENTA + text[i], end='')
            elif float(text[i]) < 10:
                print(Fore.LIGHTMAGENTA_EX + text[i], end='')
            elif float(text[i]) < 20:
                print(Fore.YELLOW + text[i], end='')
            else:
                print(Fore.YELLOW + text[i], end='')
        # print("lines number:", len(text)) # Закомментированый
        faille.close()
        print(Fore.GREEN + 'Проверка на честность. HASH =', hash1)  # Выведем HASH
        st = float(input(Fore.YELLOW + 'Сумма вашей ставки: '))  # И спросим ставку когда все сгенерировано
        while sum1 - st < 0:
            prob()
            st = float(input(Fore.YELLOW + 'Сумма вашей КОРРЕКТНОЙ ставки: '))
        sum1 -= st
        kf = float(input('Коэффицент: '))
        for i in range(len(mas)):  # Покрутили цифры)
            prob()
            if mas[i] < 1.2:
                print(Fore.RED + '╭─────ᘒ─────╮')
                print(Fore.RED + '    ', mas[i], '      ')
                print(Fore.RED + '╰─────ᘒ─────╯')
                time.sleep(.05)
            elif mas[i] < 2:
                print(Fore.BLUE + '╭─────ᘒ─────╮')
                print(Fore.BLUE + '    ', mas[i], '      ')
                print(Fore.BLUE + '╰─────ᘒ─────╯')
                time.sleep(.05)
            elif mas[i] < 3:
                print(Fore.GREEN + '╭─────ᘒ─────╮')
                print(Fore.GREEN + '    ', mas[i], '      ')
                print(Fore.GREEN + '╰─────ᘒ─────╯')
                time.sleep(.03)
            elif mas[i] < 5:
                print(Fore.MAGENTA + '╭─────ᘒ─────╮')
                print(Fore.MAGENTA + '    ', mas[i], '      ')
                print(Fore.MAGENTA + '╰─────ᘒ─────╯')
                time.sleep(.02)
            elif mas[i] < 10:
                print(Fore.LIGHTMAGENTA_EX + '╭─────ᘒ─────╮')
                print(Fore.LIGHTMAGENTA_EX + '    ', mas[i], '      ')
                print(Fore.LIGHTMAGENTA_EX + '╰─────ᘒ─────╯')
                time.sleep(.01)
            elif mas[i] < 20:
                print(Fore.YELLOW + '╭─────ᘒ─────╮')
                print(Fore.YELLOW + '    ', mas[i], '      ')
                print(Fore.YELLOW + '╰─────ᘒ─────╯')
                time.sleep(.005)
            else:
                print(Fore.YELLOW + '╭─────ᘒ─────╮')
                print(Fore.YELLOW + '    ', mas[i], '      ')
                print(Fore.YELLOW + '╰─────ᘒ─────╯')
                time.sleep(.001)
        prob()
        if kf <= mas[len(mas) - 1]:  # Выводим проигрыш или нет
            print(Fore.GREEN + 'CRUSH', mas[len(mas) - 1])
            print('Ваш выигрыш:', round(kf * st, 2))
            sum1 += round(kf * st, 2)
            print('Ваш баланс -', sum1)
            if input('Хотите проверить ставку на честность? (Да/нет)').lower() == 'да':
                print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный '
                      'HASH')
                print(salt)
                print('HASH =', hash1)
        else:
            print(Fore.RED + 'CRUSH', mas[len(mas) - 1])
            print('Ваш выигрыш: 0')
            print('Ваш баланс -', sum1)
            if input(Fore.RESET + 'Хотите проверить ставку на честность? (Да/нет)').lower() == 'да':
                print('Для проверки на честность переведите через SHA-256 данный текст и выведет в начале показанный '
                      'HASH')
                print(salt)
                print('HASH =', hash1)
        if sum1 == 0:
            print(Fore.RED + 'Вы проиграли)))')
            print('Спасибо за игру в Crush Simulator by BlackAlex')
            x = input()
            break
        else:
            faille = open('log.txt', 'a')
            faille.write(f"\n{crush}")  # Заносим краш в историю
            faille.close()
            x = input(Fore.GREEN + 'Хотите продолжить? (Да/нет)')
    else:
        print(Fore.GREEN + 'Ваш баланс -', sum1)
        if round(sum1 / sum2) >= 1:
            print('Ваша начальная сумма приумножилась в', round(sum1 / sum2, 2), 'раз(а)')
        else:
            print(Fore.RED + 'Ваша начальная сумма уменьшилась в', round(sum1 / sum2, 2), 'раз(а)')
        print('Спасибо за игру в Crush Simulator by BlackAlex')
        x = input()
