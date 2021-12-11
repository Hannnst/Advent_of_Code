
positions = []
with open("Files/day7_test.txt", "r") as f:
  for line in f:
    positions = list(map(int,line.split(',')))

print(positions)
# calculate all the different sums to shift all the positions to each position
fuels = []
sums_per_pos = []

# make 2d array for storage of sums of fuel
for x in range(len(positions)+10):
    sums_per_pos.append([])

for i,p in enumerate(positions):
    
    for i2,p2 in enumerate(positions):
        sum = 0
        #print("sum is reset")
        tax = 1
        print("Moves from ", p, " to ", p2)
        for x in range(abs(p-p2)): # for every step, add +1x tax to the sum
            sums_per_pos[p] = [] # each position has an array of sums for each pos they go to
            sum += tax
            tax += 1 # part 2
        print("sum for movement: ", sum, "p2", p2)
        sums_per_pos[i2].append(sum)
    fuels.append(sum)

#print("fuels:", fuels)
#minimal = min(fuels.values())
#minimal_index = list(fuels.keys())[list(fuels.values()).index(minimal)]
#print("The position that requires the least fuel for the crabs is", minimal, " at index ", minimal_index ) # part 1


# Part 2
#print("Sum of all fuels is ", fuels)
print("sums per pos is ", sums_per_pos)
sumFuel = 0
for v in fuels:
    sumFuel += v
print(sumFuel)

