"""--- Day 6: Guard Gallivant ---
The Historians use their fancy
device
again, this time to whisk you all away to the North Pole prototype suit manufacturing lab... in the year
1518
! It turns out that having direct access to history is very convenient for a group of historians.
You still have to be careful of time paradoxes, and so it will be important to avoid anyone from 1518 while The Historians search for the Chief. Unfortunately, a single
guard
is patrolling this part of the lab.
Maybe you can work out where the guard will go ahead of time so that The Historians can search safely?
You start by making a map (your puzzle input) of the situation. For example:
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
The map shows the current position of the guard with
^
(to indicate the guard is currently facing
up
from the perspective of the map). Any
obstructions
- crates, desks, alchemical reactors, etc. - are shown as
#
.
Lab guards in 1518 follow a very strict patrol protocol which involves repeatedly following these steps:
If there is something directly in front of you, turn right 90 degrees.
Otherwise, take a step forward.
Following the above protocol, the guard moves up several times until she reaches an obstacle (in this case, a pile of failed suit prototypes):
....#.....
....^....#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Because there is now an obstacle in front of the guard, she turns right before continuing straight in her new facing direction:
....#.....
........>#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#...
Reaching another obstacle (a spool of several
very
long polymers), she turns right again and continues downward:
....#.....
.........#
..........
..#.......
.......#..
..........
.#......v.
........#.
#.........
......#...
This process continues for a while, but the guard eventually leaves the mapped area (after walking past a tank of universal solvent):
....#.....
.........#
..........
..#.......
.......#..
..........
.#........
........#.
#.........
......#v..
By predicting the guard's route, you can determine which specific positions in the lab will be in the patrol path.
Including the guard's starting position
, the positions visited by the guard before leaving the area are marked with an
X
:
....#.....
....XXXXX#
....X...X.
..#.X...X.
..XXXXX#X.
..X.X.X.X.
.#XXXXXXX.
.XXXXXXX#.
#XXXXXXX..
......#X..
In this example, the guard will visit
41
distinct positions on your map.
Predict the path of the guard.
How many distinct positions will the guard visit before leaving the mapped area?"""

# template.py
def main():
    """Main function to execute the solution for Day 6.""""
    with open('input_day6.txt', 'r') as f:
        data = f.read().strip().split('\\n')

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))

def part1(data):
    """Solve Part 1 of Day 6 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 1 of the task.
    """
    # TODO: Implement solution for Part 1
    pass

def part2(data):
    """Solve Part 2 of Day 6 task.

    Args:
        data (list): List of strings representing the input data.

    Returns:
        The solution to Part 2 of the task.
    """
    # TODO: Implement solution for Part 2
    pass

if __name__ == "__main__":
    main()