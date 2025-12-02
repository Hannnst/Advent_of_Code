'''
First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes.
This increases the energy level of all adjacent octopuses by 1,
including octopuses that are diagonally adjacent.

If this causes an octopus to have an energy level greater than 9, it also flashes.
This process continues as long as new octopuses keep having their energy level increased beyond 9.
(An octopus can only flash at most once per step.)

Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

Adjacent points will be affected. All affected points will then be:
That means:
[x-1][y-1] [x][y-1] [x+1][y-1]
[x-1][y]   [x][y]   [x+1][y]  
[x-1][y+1] [x][y+1] [x+1][y+1]

For each octopus, if number > 9, run method:
Count x/y around given coordinate and increase value by 1

run method again until there's noone < 9
This may be automatic with the if test or a while loop
'''
import numpy as np

def get_input(input_file_name):
    return np.genfromtxt(input_file_name, delimiter=1, dtype=int)


def get_neighbours(x):
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == j == 0:
                pass
            elif (x[0] + i) < 0 or (x[1] + j) < 0 or (x[0] + i) > 9 or (x[1] + j) > 9:
                pass
            else:
                neighbours.append([x[0] + i, x[1] + j])
    return neighbours

def flash(array, sync):
    count = 0
    for i in range(1, array.size * 10):
        array += 1
        while array.max() > 9:
            x = np.argwhere(array > 9)
            for y in x:
                array[y[0], y[1]] = 0
                for neighbour in get_neighbours(y):
                    if array[neighbour[0], neighbour[1]] != 0:
                        array[neighbour[0], neighbour[1]] += 1 # increase energy of octo
        count += np.count_nonzero(array == 0) # increase count
        if np.count_nonzero(array == 0) == array.size:
            return i
        if i == array.size and not sync:
            return count

def part1(array, sync):
    return flash(array, sync)

def part2(array, sync):
    return flash(array, sync)

print(f'Part1: {part1(get_input("Files/day11.txt"), False)}')
print(f'Part2: {part2(get_input("Files/day11.txt"), True)}')
