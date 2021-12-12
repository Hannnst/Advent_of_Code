
positions = []
with open("Files/day7.txt", "r") as f:
  for line in f:
    positions = list(map(int,line.split(',')))

'''
# calculate all the different sums to shift all the positions to each position
fuels = []
sums_per_pos = []
# make 2d array for storage of sums of fuel
for x in range(len(positions)+10):
    sums_per_pos.append([])

for i,p in enumerate(positions):
    for i2,p2 in enumerate(positions):
        sum = 0
        tax = 1
        for x in range(abs(p-p2)): # for every step, add +1x tax to the sum
            sums_per_pos[p] = [] # each position has an array of sums for each pos they go to
            sum += tax
            tax += 1 # part 2
        sums_per_pos[i2].append(sum)
    fuels.append(sum)
'''
# robin sin løsning på summering:
# calculate all the different sums to shift all the positions to each position
fuels = []

# 2d array for storage of sums of fuel
sums_per_pos = []
for x in range(max(positions) + 1):
    sums_per_pos.append([])
for p0 in positions:
    for p1 in range(max(positions) + 1):
        s = 0
        tax = 1
        for x in range(abs(p0 - p1)): # for every step, add +1x tax to the sum
            s += tax
            tax += 1 # part 2
        sums_per_pos[p1].append(s)
total_sums_per_pos = []
for p1 in range(max(positions) + 1):
    tot = sum(sums_per_pos[p1])
    total_sums_per_pos.append(tot)

print("the least fuel used would be ", min(total_sums_per_pos))


