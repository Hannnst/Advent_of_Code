from utils import readFile


def scrapCardEvaluator():
    cards = readFile("Files/day4_test.txt")
    for card in cards:
        winning_numbers = card.split(":")[1].split("|")[0]
        given_numbers = card.split(":")[1].split("|")[1]

        print(winning_numbers)
        print(given_numbers)

scrapCardEvaluator()

