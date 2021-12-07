allLines = []
matrix = []
#0,9 -> 0,5 = x1,y1 -> x2,y2
xcoordinates = []
ycoordinates = []
coordinate_pair = []
height = 0
width = 0
with open("dat5data.txt", "r") as a_file:
    for line in a_file:
        data = line.strip().replace(" ", "").split('->')
        allLines.append(data)

#print(allLines)
for line in allLines:
    cor1 = line[0].split(',')
    cor2 = line[1].split(',')
    
    xcoordinates.append(cor1[0])
    xcoordinates.append(cor2[0])
    ycoordinates.append(cor1[1])
    ycoordinates.append(cor2[1])
    coordinate_pair.append({
        'x1': int(cor1[0]),
        'y1': int(cor1[1]),
        'x2' : int(cor2[0]),
        'y2' : int(cor2[1])})

height = int(max(xcoordinates))
width = int(max(ycoordinates))

#print(height, width) # diagram dimensions

# make the matrix
for x in range(height+1000):
    matrix.append([0])
    for y in range(width+1000):
        matrix[x].append(0)

for line in matrix:
    print(line)

def iterateMatrix(cor1, cor2, static, val):
    print("irerate ", val)
    if cor1<cor2: # increment
        for x in range((cor2-cor1)+1): # +1 because the last index should also be affected
                if val == 'x':
                    matrix[static][cor1+x] = matrix[static][cor1+x] + 1
                else:
                    matrix[cor1+x][static] = matrix[cor1+x][static] + 1
    else: # decrement
        for x in range((cor1-cor2)+1): # +1 because the last index should also be affected
                if val == 'x': # for x
                    matrix[static][cor1-x] = matrix[static][cor1-x] + 1
                else: # for y
                    matrix[cor1-x][static] = matrix[cor1-x][static] + 1

def matrixGo(x1, y1, x2, y2):
    '''
    need to check if x1 < x2
    if positive, counter should increase from x1 until x2
    if negative, counter should decrease until x2
    '''
    print("coordinates given: ", x1, y1, x2, y2)
    countX = 0
    countY = 0
    if y1 == y2:
        iterateMatrix(x1,x2,y1, 'x')
    elif x1==x2:
        iterateMatrix(y1,y2,x1, 'y')
    

for cor in coordinate_pair:
    #print(cor)
    #print(cor['y2'])
    matrixGo(cor['x1'], cor['y1'], cor['x2'], cor['y2'])

# how many points?
points = 0
for line in matrix:
    print(line)
    for number in line:
        if number > 1:
            points = points + 1
print("\nPOINTS: ", points)


