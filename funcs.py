import random as rndm


def indt(ind):
    print("----"*ind)


def gameMode(maxNumber, tries):
    guessNumber = rndm.randint(0, maxNumber)
    guessTry = 0
    while guessTry < tries:
        guessInput = int(input("Введите предпологаемое число: "))
        indt(4)
        guessTry += 1
        guessTryLeft = tries - guessTry
        if guessInput < guessNumber:
            print("Неверно!")
            print(
                "Подсказка: Число больше, чем {}!" .format(guessInput))
            print("Всего попыток:", tries)
            print("Осталось попыток:", guessTryLeft)
            print("Кол-во использованных попыток:", guessTry)
            indt(4)
            continue
        elif guessInput > guessNumber:
            print("Неверно!")
            print(
                "Подсказка: Число меньше, чем {}!" .format(guessInput))
            print("Всего попыток:", tries)
            print("Осталось попыток:", guessTryLeft)
            print("Кол-во использованных попыток:", guessTry)
            indt(4)
            continue
        elif guessInput == guessNumber:
            print("Правильно!!!")
            print("Кол-во использованных попыток:", guessTry)
            indt(4)
            break
        if guessTry >= tries:
            print("Вы проиграли!")
            print("Кол-во использованных попыток:", guessTry)
            indt(4)
            break
