'''
So, suppose you have a lanternfish with an internal timer value of 3:

    After one day, its internal timer would become 2.
    After another day, its internal timer would become 1.
    After another day, its internal timer would become 0.
    After another day, its internal timer would reset to 6, and it would create a new lanternfish with an internal timer of 8.
    After another day, the first lanternfish would have an internal timer of 5, and the second lanternfish would have an internal timer of 7.

    A lanternfish that creates a new fish resets its timer to 6, not 7 (because 0 is included as a valid timer value).
    The new lanternfish starts with an internal timer of 8 and does not start counting down until the next day.
'''
from typing import Deque
import numpy as np
lanternfish = []
with open("Files/day6.txt", "r") as f:
  for line in f:
      lanternfish = list(map(int,line.split(','))) # reads first line and converts it to int list

print(lanternfish)
from collections import deque


'''
input: [2,4,5,5,1]
Example:
[0,0,0,0,0,0,0,0,0]
0 1 2 3 4 5 6 7 8 9

with given input it will be
[0,1,1,0,1,2,0,0,0]

After some iterations:
[1,1,0,1,2,0,0,0,0] # here's 1 at the index 0, where the fish is value 0, and creates 1 each fish at index 9.
[1,0,1,2,0,0,1,0,1] # 1 more fish at index 9, one more at index 6. Again a fish is at 0 and the same process happens
[0,1,2,0,0,1,1,1,1] # every time the entire row sort of shifts to the left and each time fish is at index 0, the same
amount of fish gets created at index 9 and the fish from index 0 gets moved to index 6.

Each round:
Shift all values index-1
index 6, 9 += fish[0]
'''
# Counts days and adds new fish to the lanternfish-list according to the logic
fishCount = [0,0,0,0,0,0,0,0,0]
days = 0
for x in range(256):
    days =  x
    #print("day ", days)
    #print("fishes today: ", lanternfish)
    # for each fish, check number and if fish is a number between 8 and 0, increase the number
    # on the index of the lanternfishCount-array
    # When the number on index 9
    '''for i,fish in enumerate(lanternfish):
        if fish == 0:
            lanternfish[i] = 6
            lanternfish.append(9) # sets to 9 because it's easier if counting happens right away

        else: lanternfish[i] = lanternfish[i] - 1 # for the next day

        # using the lanternfishCount array instead:
        for i in range(10): # for as many times as asked
            temp1 = []
            temp2 = []
            # create two temp arrats for rotating
            for x in range(len(fishCount)):
                if x < 7: temp1.append(fishCount[x])
                else: temp1.append(fishCount[x])
            # first, shift temp1 one to the left so 0 becomes 6 etc. Then shift temp2 and set temp1[6] += temp2[1]
            fishToAddTo6 = fishCount[0] # all fish on 0 turns into fish on count 6, saves this value to use
            for i,fish in enumerate(fishCount):
                np.roll(temp1,-1)
                temp1.extend(temp2)
                # must move index 7-9 one to the left, with the entire array combined
                for index, fish in temp2:
                    temp1[len(temp2)+index] += fish # index 6 gets index 7 etc. Must remove the content from current index after
                    temp1[len(temp2)+index]
                    temp2[index]
                

                
                # can make an own temp array consisting of all values from 0-6 and rotate these 1 time
                # before puttin the 0-6 and 7-9 arrays together again
                if fish == 0:
                    lanternfish[i] = 6
                    lanternfish.append(9) # sets to 9 because it's easier if counting happens right away

            else: lanternfish[i] = lanternfish[i] - 1 # for the next day
            '''

MIN_VAL = 0
RESET_VAL = 6
NEW_VAL = 8

def part_two(input):
    def simulate_fish(input, total_days):
        state = [int(n) for n in input.readline().strip().split(',')]
        fish_on_day = Deque([0] * (NEW_VAL+1))
        for val in state: fish_on_day[val] = fish_on_day[val]+1
        for _ in range(total_days):
            zero_day_fish = fish_on_day[0]
            fish_on_day[NEW_VAL-1] += zero_day_fish
            fish_on_day.rotate(-1)
        return(sum(fish_on_day))
    return simulate_fish(input, 256)

if __name__ == '__main__':
    with open('Files/day6.txt', 'r') as input:
        print("Part 1: Lanternfish amount after ", days+1, " days: ", len(lanternfish))
        print(f'Part 2: {part_two(input)} is the solution')
            
    


