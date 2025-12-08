"""--- Day 4: Printing Department ---
You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really
big
print jobs).
Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
"Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
The rolls of paper (
@
) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
For example:
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
The forklifts can only access a roll of paper if there are
fewer than four rolls of paper
in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
In this example, there are
13
rolls of paper that can be accessed by a forklift (marked with
x
):
..xx.xx@x.
x@@.@.@.@@
@@@@@.x.@@
@.@@@@..@.
x@.@@@@.@x
.@@@@@@@.@
.@.@.@.@@@
x.@@@.@@@@
.@@@@@@@@.
x.x.@@@.x.
Consider your complete diagram of the paper roll locations.
How many rolls of paper can be accessed by a forklift?"""

# template.py
def main():
    with open('files/day4.txt', 'r') as f:
        data = f.read().strip().split('\n')

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    forkable = 0
    horizontal_size = len(data[0])
    vertical_size = len(data)
    for y in range(vertical_size):
        for x in range(horizontal_size):
            roll = data[y][x]
            if roll == '@':
                adjacents = findAdjacent(x, y, data, horizontal_size, vertical_size)
                count_rolls = adjacents.count('@')
                if count_rolls < 4:
                    forkable += 1
    return forkable

def findAdjacent(x, y, data, horizontal_size, vertical_size):
    adjacent_positions = [(-1, -1), (0, -1), (1, -1),
                          (-1, 0),          (1, 0),
                          (-1, 1),  (0, 1),  (1, 1)]
    adjacents = []
    for exes, dykes in adjacent_positions:
        if 0 <= x+exes < horizontal_size and 0 <= y+dykes < vertical_size:
            adjacents.append(data[y+dykes][x+exes])
    return adjacents


def part2(data):
    # Convert strings to lists so we can modify them
    data = [list(row) for row in data]
    horizontal_size = len(data[0])
    vertical_size = len(data)
    total_removed = 0
    
    # Keep repeating until no more rolls can be removed
    while True:
        removed_this_round = 0
        rolls_to_remove = []
        
        # Find all rolls that can be accessed in this round
        for y in range(vertical_size):
            for x in range(horizontal_size):
                roll = data[y][x]
                if roll == '@':
                    adjacents = findAdjacent(x, y, data, horizontal_size, vertical_size)
                    count_rolls = adjacents.count('@')
                    if count_rolls < 4:
                        rolls_to_remove.append((x, y))
        
        # Remove all accessible rolls found in this round
        for x, y in rolls_to_remove:
            data[y][x] = '.'
            removed_this_round += 1
            total_removed += 1
        
        # If no rolls were removed this round, we're done
        if removed_this_round == 0:
            break
    
    return total_removed

if __name__ == "__main__":
    main()