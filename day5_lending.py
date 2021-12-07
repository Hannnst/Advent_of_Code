from time import time
import re
start = time()

with open("dat5data.txt") as f:
    raw_data = f.readlines()

parser = re.compile(r"""(?P<x1>\d+),(?P<y1>\d+) -> (?P<x2>\d+),(?P<y2>\d+)""")

lines = [parser.search(data).groupdict() for data in raw_data]
lines = [ {k:int(v) for k,v in ln.items() } for ln in lines]

def draw_line(grid, x1=0, y1=0, x2=0, y2=0, diags=False):
    if x1==x2:
        if y2 < y1:
            y1, y2 = y2, y1
        for y in range(y1, y2+1):
            grid[x1][y] += 1
    elif y1==y2:
        if x2 < x1:
            x1, x2 = x2, x1
        for x in range(x1, x2+1):
            grid[x][y1] += 1
    elif diags:
        if x2 < x1:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        y = y1
        step = 1 if y2>y1 else -1
        for x in range(x1, x2+1):
            grid[x][y] += 1
            y += step

    return grid

#### PART 1

terrain = [ [ 0 for i in range(1000) ] for j in range(1000) ]

for ln in lines:
    terrain = draw_line(terrain, **ln)

count = 0
for rw in terrain:
    for i in rw:
        if i > 1:
            count += 1

print("\nThere are {} points at which at least two lines overlap".format(count))
print("Runtime: {} seconds\n".format(time()-start))

#### PART 2

start = time()

terrain = [ [ 0 for i in range(1000) ] for j in range(1000) ]

for ln in lines:
    terrain = draw_line(terrain, **ln, diags=True)

count = 0
for rw in terrain:
    for i in rw:
        if i > 1:
            count += 1

print("There are {} points at which at least two lines overlap, including diagonals".format(count))
print("Runtime: {} seconds\n".format(time()-start))