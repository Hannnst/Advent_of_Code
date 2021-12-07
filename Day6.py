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
lanternfish = []
with open("Files/day6.txt", "r") as f:
  for line in f:
      lanternfish = list(map(int,line.split(','))) # reads first line and converts it to int list

print(lanternfish)

# Counts days and adds new fish to the lanternfish-list according to the logic
days = 0
for x in range(256):
    days =  x
    #print("day ", days)
    #print("fishes today: ", lanternfish)
    for i,fish in enumerate(lanternfish):
        if fish == 0:
            lanternfish[i] = 6
            lanternfish.append(9) # sets to 9 because it's easier if counting happens right away
        else: lanternfish[i] = lanternfish[i] - 1 # for the next day
        
    
print("Lanternfish amount after ", days+1, " days: ", len(lanternfish))

