
''' Find points where all neighbours are higher than themselves and sum there numbers '''
points = []
low_points = []
# save all digits in 2d array
with open("Files/day9.txt", "r") as f:
  for line in f:
    temp = []
    for digit in line.strip():
      temp.append(int(digit))
    points.append(temp)

# matrix
#for p in points:
#  print(p)

# For point in the matrix, say point [2][2], we have to check for every neighbour
# in this case it would be
'''
       [2][1] 
[1][2] [2][2] [3][2]
       [2][3] 

That means:
         [x][y-1] 
[x-1][y]  [x][y]  [x+1][y]  
         [x][y+1] 
'''


for x in range(len(points)):
  for y in range(len(points[x])):
    neighbours = []
    if x < len(points)-1:
      neighbours.append(points[x+1][y])
    if y < len(points[x])-1:
      neighbours.append(points[x][y+1])
    if x > 0:
      neighbours.append(points[x-1][y])
    if y > 0:
      neighbours.append(points[x][y-1])

    # all neighbours added, ready for comparison
    if all([points[x][y] < n for n in neighbours]):
      low_points.append({'x': x, 'y': y, 'p': points[x][y]})

sum_low = sum([m['p'] for m in low_points]) + len(low_points)
print("sum of low points is ", sum_low)
# part 2
''' A basin is all locations that eventually flow downward to a single low point. Therefore, every low point has a basin,
although some basins are very small. Locations of height 9 do not count as being in any basin, and all other locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the low point. The example above has four basins.
'''

# we have a list of all low points, we can loop through them and use their coordinates
def helloThereNeighbour(point):
    neighbours = []
    basin = [point]
    counter = 0
    x = point['x']
    y = point['y']
    if x < len(points)-1:
      if points[x+1][y] not in basin:
        neighbours.append({'x': x+1, 'y': y, 'p': points[x+1][y]})
    if y < len(points[x])-1:
      if points[x][y+1] not in basin:
        neighbours.append({'x': x, 'y': y+1, 'p': points[x][y+1]})
    if x > 0:
      if points[x-1][y] not in basin:
        neighbours.append({'x': x-1, 'y': y, 'p': points[x-1][y]})
    if y > 0:
      if points[x][y-1] not in basin:
        neighbours.append({'x': x, 'y': y-1, 'p': points[x][y-1]})

    # check if any neighbour is the same as current point + 1
    # run func on point if true
    for n in neighbours:
      if n['p'] == point['p'] + 1 and n['p'] != 9:
        counter += 1
        basin += (helloThereNeighbour(n))
    return basin


allBasin = []
print("low points: ", low_points)
for p in low_points:
  allBasin.append(helloThereNeighbour(p))

uniqueBasins = []
lengths = []
# must remove duplicate points from all basin
for b in allBasin:
  uniqueBasin = []
  for p in b:
    if p not in uniqueBasin:
      uniqueBasin.append(p)
  # want the largest basins to be in front in the array uniquebasins
  index = 0
  for ub in uniqueBasins:
    if len(uniqueBasin) > ub['len']:
      print
  lengths.append(len(uniqueBasin))
  uniqueBasins.append({'basin':uniqueBasin, 'len':len(uniqueBasin)})

# sorting and popping the three last numbers in all lengths
sortedLens = sorted(lengths)
a, b, c = sortedLens.pop(), sortedLens.pop(), sortedLens.pop()
print("the three basins are ", a,b,c)
print("The three lengths of the largest basins is ", a*b*c)


