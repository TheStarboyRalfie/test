from funcs import indt, gameMode
print("Игра 'Угадай число'")
print("Добро пожаловать!")
gameActive = True
while gameActive:
    gameDifficulties = ["/easy", "/medium", "/hard"]
    print("Выберите уровень сложности, чтобы начать игру (/easy /medium /hard):")
    gameDifficulty = input(str())
    print("Выбран режим сложности {}" .format(gameDifficulty))
    indt(4)
    if gameDifficulty in gameDifficulties:
        if gameDifficulty == "/easy":
            gameMode(10, 4)
        elif gameDifficulty == "/medium":
            gameMode(25, 8)
        elif gameDifficulty == "/hard":
            gameMode(50, 16)
