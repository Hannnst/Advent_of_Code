from utils import readFile
import re

def find_spelled_out_numbers(line):
    # Use regular expression to find spelled-out numbers
    matches = re.findall(r'[a-zA-Z]*(zero|one|two|three|four|five|six|seven|eight|nine)[a-zA-Z]*', line)

    # Convert spelled-out numbers to digits
    numbers = [str(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(match)) for match in matches]

    return numbers
def artisticArtElfDecoder():
    """ What it do """
    calibrationValues = readFile("Files/day1_test.txt")
    sum = 0
    sum9000 = 0
    for calibration in calibrationValues:
        numbers = []
        numbers9000 = []
        potentialNumber = ""
        for sign in calibration:
            try:
                if sign.isnumeric():
                    numbers.append(int(sign))
                else:
                    print(potentialNumber)
                    potentialNumber += sign
                    if artisticArtElfDecoder9000(potentialNumber):
                        print(potentialNumber)
                        artisticArtElfDecoder9000(potentialNumber)
                        numbers9000.append(artisticArtElfDecoder9000(potentialNumber))
                        potentialNumber = ""
            except:
                pass
        if (len(numbers) > 0):
            sum += int(str(numbers[0]) + str(numbers.pop()))
        if (len(numbers9000) > 1):
            sum9000 += int(str(numbers9000[0]) + str(numbers9000.pop()))

    return sum, sum9000

def artisticArtElfDecoder9000(number):
    numbers = {
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "ten" : 10
    }
    return numbers[number]

import re

def find_spelled_out_numbers(line):
    matches = re.findall(r'[a-zA-Z]*(zero|one|two|three|four|five|six|seven|eight|nine)[a-zA-Z]*', line)
    numbers = [str(['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'].index(match)) for match in matches]
    return numbers

def combine_numbers(numbers):
    return int(''.join(numbers))

def main():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]

    combined_numbers = []

    for line in lines:
        numbers = find_spelled_out_numbers(line)

        if numbers:
            combined_number = combine_numbers(numbers)
            combined_numbers.append(combined_number)

    total_sum = sum(combined_numbers)

    print("Combined Numbers:", combined_numbers)
    print("Total Sum:", total_sum)

if __name__ == "__main__":
    main()


print(artisticArtElfDecoder())