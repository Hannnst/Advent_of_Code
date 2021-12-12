'''
First, the energy level of each octopus increases by 1.
Then, any octopus with an energy level greater than 9 flashes. This increases the energy level of alladjacent octopuses by 1,
including octopuses that are diagonally adjacent. If this causes an octopus to have an energy level greater than 9, it also flashes.
This process continues as long as new octopuses keep having their energy level increased beyond 9.
(An octopus can only flash at most once per step.)
Finally, any octopus that flashed during this step has its energy level set to 0, as it used all of its energy to flash.

Adjacent points will be affected. All affected points will then be:
That means:
 [x-1]     [x][y-1] [x+1][y-1]
[x-1][y]   [x][y]   [x+1][y]  
[x-1][y+1] [x][y+1] [x+1][y+1]
'''
