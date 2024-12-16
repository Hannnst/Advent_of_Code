"""--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the
Ceres monitoring station
!
As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her
word search
(your puzzle input). She only has to find one word:
XMAS
.
This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of
XMAS
- you need to find
all of them
. Here are a few ways
XMAS
might appear, where irrelevant characters have been replaced with
.
:
..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search,
XMAS
occurs a total of
18
times; here's the same word search again, but where letters not involved in any
XMAS
have been replaced with
.
:
....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
Take a look at the little Elf's word search.
How many times does
XMAS
appear?"""

# template.py
def main():
    """Main function to execute the solution for Day 4.""""
    with open('input_day4.txt', 'r') as f:
        data = f.read().strip().split('\\n')

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    """Solve Part 1 of Day 4 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 1 of the task.
    """
    # TODO: Implement solution for Part 1
    pass

def part2(data):
    """Solve Part 2 of Day 4 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 2 of the task.
    """
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
    main()