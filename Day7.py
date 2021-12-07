positions = []
with open("Files/day7_test.txt", "r") as f:
  for line in f:
    positions = list(map(int,line.split(',')))

print(positions)
# calculate all the different sums to shift all the positions to each position
fuels = {}

for i,p in enumerate(positions):
    sum = 0
    tax = 0
    for i2,p2 in enumerate(positions):
        sum = sum + (abs(p-p2)) + tax
        tax += 1 # part 2
    fuels[i] = sum

#print("fuels:", fuels)
minimal = min(fuels.values())
minimal_index = list(fuels.keys())[list(fuels.values()).index(minimal)]

print("The position that requires the least fuel for the crabs is", minimal, " at index ", minimal_index ) # part 1

# Part 2
print("Sum of all fuels is ", fuels.values())
sumFuel = 0
for v in fuels.values():
    sumFuel += v
print(sumFuel)


