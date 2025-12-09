<<<<<<< HEAD
"""--- Day 3: Lobby ---
You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all
offline
.
"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."
You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also
offline
."
"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."
There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their
joltage
rating, a value from
1
to
9
. You make a note of their joltage ratings (your puzzle input). For example:
987654321111111
811111111111119
234234234234278
818181911112111
The batteries are arranged into
banks
; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on
exactly two
batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like
12345
and you turn on batteries
2
and
4
, the bank would produce
24
jolts. (You cannot rearrange batteries.)
You'll need to find the largest possible joltage each bank can produce. In the above example:
In
98
7654321111111
, you can make the largest joltage possible,
98
, by turning on the first two batteries.
In
8
1111111111111
9
, you can make the largest joltage possible by turning on the batteries labeled
8
and
9
, producing
89
jolts.
In
2342342342342
78
, you can make
78
by turning on the last two batteries (marked
7
and
8
).
In
818181
9
1111
2
111
, the largest joltage you can produce is
92
.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is
98
+
89
+
78
+
92
=
357
.
There are many batteries in front of you. Find the maximum joltage possible from each bank;
what is the total output joltage?"""

# template.py
def main():
    with open('files/day3.txt', 'r') as f:
        data = [line.strip() for line in f]

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    joltages = []
    for bank in data:
        max_joltage = 0
        
        # Try all possible pairs of digits in order
        for i in range(len(bank)):
            for j in range(i + 1, len(bank)):
                # Form 2-digit number from positions i and j
                two_digit = int(bank[i] + bank[j])
                max_joltage = max(max_joltage, two_digit)
        
        joltages.append(max_joltage)
    return sum(joltages)


def part2(data):
    joltages = []
    for bank in data:
        digits = list(bank)
        
        # We need to remove (len - 12) digits to get exactly 12
        to_remove = len(digits) - 12
        
        # Use a greedy approach: for each removal, find the digit that
        # when removed, gives us the largest remaining number
        for _ in range(to_remove):
            best_removal = 0
            best_value = 0
            
            # Try removing each digit and see which gives the largest number
            for i in range(len(digits)):
                temp_digits = digits[:i] + digits[i+1:]  # Remove digit at position i
                if temp_digits:  # Make sure we don't have an empty list
                    temp_value = int(''.join(temp_digits))
                    if temp_value > best_value:
                        best_value = temp_value
                        best_removal = i
            
            # Remove the digit that gives us the best result
            digits.pop(best_removal)
        
        # Form the 12-digit joltage number
        max_joltage = int(''.join(digits))
        joltages.append(max_joltage)    
    return sum(joltages)

if __name__ == "__main__":
=======
"""--- Day 3: Lobby ---
You descend a short staircase, enter the surprisingly vast lobby, and are quickly cleared by the security checkpoint. When you get to the main elevators, however, you discover that each one has a red light above it: they're all
offline
.
"Sorry about that," an Elf apologizes as she tinkers with a nearby control panel. "Some kind of electrical surge seems to have fried them. I'll try to get them online soon."
You explain your need to get further underground. "Well, you could at least take the escalator down to the printing department, not that you'd get much further than that without the elevators working. That is, you could if the escalator weren't also
offline
."
"But, don't worry! It's not fried; it just needs power. Maybe you can get it running while I keep working on the elevators."
There are batteries nearby that can supply emergency power to the escalator for just such an occasion. The batteries are each labeled with their
joltage
rating, a value from
1
to
9
. You make a note of their joltage ratings (your puzzle input). For example:
987654321111111
811111111111119
234234234234278
818181911112111
The batteries are arranged into
banks
; each line of digits in your input corresponds to a single bank of batteries. Within each bank, you need to turn on
exactly two
batteries; the joltage that the bank produces is equal to the number formed by the digits on the batteries you've turned on. For example, if you have a bank like
12345
and you turn on batteries
2
and
4
, the bank would produce
24
jolts. (You cannot rearrange batteries.)
You'll need to find the largest possible joltage each bank can produce. In the above example:
In
98
7654321111111
, you can make the largest joltage possible,
98
, by turning on the first two batteries.
In
8
1111111111111
9
, you can make the largest joltage possible by turning on the batteries labeled
8
and
9
, producing
89
jolts.
In
2342342342342
78
, you can make
78
by turning on the last two batteries (marked
7
and
8
).
In
818181
9
1111
2
111
, the largest joltage you can produce is
92
.
The total output joltage is the sum of the maximum joltage from each bank, so in this example, the total output joltage is
98
+
89
+
78
+
92
=
357
.
There are many batteries in front of you. Find the maximum joltage possible from each bank;
what is the total output joltage?"""

# template.py
def main():
    with open('input_day3.txt', 'r') as f:
        data = f.read().strip().split('\\n')

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    """Solve Part 1 of Day 3 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 1 of the task.
    """
    # TODO: Implement solution for Part 1
    pass

def part2(data):
    """Solve Part 2 of Day 3 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 2 of the task.
    """
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
>>>>>>> 4b2cb12631ddb875d0d4c1100321d33e74a63f34
    main()