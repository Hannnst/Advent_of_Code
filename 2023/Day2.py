""" only 12 red cubes, 13 green cubes, and 14 blue cubes? """
from collections import defaultdict
from utils import readFile

inventory = {
    "red": 12,
    "green": 13,
    "blue": 14
}
def cubeGame(inventory):
    """ What it does """
    totalCubes = sum(inventory.values())

    sentence = "Game 75: 13 blue, 20 red, 10 green; 3 green, 5 blue, 14 red; 9 red, 13 green, 7 blue; 1 blue, 15 red, 2 green; 11 blue, 2 green, 17 red; 11 red, 13 blue, 13 green"
    for line in readFile("Files/day2_test.txt"):
        # Extract color and count information from the sentence
        for info in sentence.split(';'):
            for cubeGrab in info.split(','):
                color, count = cubeGrab.strip().split()
                inventory[color] += int(count)

cubeGame(inventory)
print(totalCubes)
