import numpy as np
lines = []
matrix = []
coordinate_pair = []

# read file
with open("Files/day5.txt", "r") as a_file:
    for line in a_file:
        data = line.strip().replace(" ", "").split('->')
        lines.append(data)

#initialize map
matrix = np.zeros((1000,1000))

# Making int-dict with all coordinates from file
for line in lines:
    cor1 = line[0].split(',')
    cor2 = line[1].split(',')
    
    coordinate_pair.append({
        'x1': int(cor1[0]),
        'y1': int(cor1[1]),
        'x2' : int(cor2[0]),
        'y2' : int(cor2[1])})

# Printing matrix in two possible different ways
def printM():
    for line in matrix:
        print(line)
        #for n, i in enumerate(line):
            #if i == 0:
                #line[n] = '.'
        #print(line)

def iterateMatrix(x1,y1,x2,y2):
    ''' Should take in x1,y1, x2,y2 and count both for x and y values so that 
    values may be implemented diagnonally as well as horizontally/vertically
    9,7 -> 7,9 will be 9-7, or abs(7-9)
    '''
    #print("Coordinates: ", x1, y1, "->", x2, y2)
    x = x1 
    y = y1
    while x!=x2 or y!=y2:
        matrix[x][y] +=1
        if x != x2:
            if x1<x2: x += 1
            elif x1>x2: x -= 1
        if y != y2:
            if y1<y2: y += 1
            elif y1>y2: y -= 1
        matrix[x][y] += 1
         
for cor in coordinate_pair:
    iterateMatrix(cor['x1'], cor['y1'], cor['x2'], cor['y2'])

points = (matrix > 1).sum()
print("\nPOINTS: ", points)


