from utils import readFile

inventory = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def cubeGame(inventory: dict):
    legitimateGames = 0
    schizoGames = 0
    for line in readFile("Files/day2.txt"):
        gameID = line.split(":")[0].split().pop()
        schizoGames += schizoGame(line)
        if bogusDetector(line, inventory):
            print(f"Game {gameID} is possible")
            legitimateGames += (int(gameID))
    return legitimateGames, schizoGames

def bogusDetector(line: str, inventory: dict) -> bool:
    cubeGrab = line.split(":")[1].split(";")
    for cube in cubeGrab:
        for combination in cube.split(','):
            num, color = combination.split()
            if int(num) > inventory[color]:
                return False
    return True

def schizoGame(line: str):
    game = {}
    cubeGrab = line.split(":")[1].split(";")
    power = 1
    for cube in cubeGrab:
        for combination in cube.split(','):
            num, color = combination.split()
            if color in game:
                if int(num) > game[color]:
                    game[color] = int(num)
            else:
                game[color] = int(num)
    for numbers in game.values():
        power *= numbers
    return power

print(cubeGame(inventory))