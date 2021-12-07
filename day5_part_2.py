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
    
    # only for calculating dimensions of the board
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


# how many points?
def printM():
    points = 0
    for line in matrix:
        print(line)
        for number in line:
            if number > 1:
                points = points + 1
        #for n, i in enumerate(line):
            #if i == 0:
                #line[n] = '.'
        #print(line)
    print("\nPOINTS: ", points)


def iterateMatrix(x1,y1,x2,y2):
    ''' SHould take in x1,y1, x2,y2 and count both for x and y values so that 
    values may be implemented diagnonally as well as horizontally/vertically
    9,7 -> 7,9 will be 9-7, or abs(7-9)
    '''
    #print("Coordinates: ", x1, y1, "->", x2, y2)
    x = x1 # must start at 1 less than given because we count from one too high...
    y = y1
    # linear /horizontal
    if y1==y2:
        cor1 = x1
        cor2 = x2
        static = y1
        if cor1<cor2: # increment
            for x in range((cor2-cor1)+1): # +1 because the last index should also be affected
                    matrix[static][cor1+x] = matrix[static][cor1+x] + 1 # for x     
        else: # decrement
            for x in range((cor1-cor2)+1): # +1 because the last index should also be affected
                    matrix[static][cor1-x] = matrix[static][cor1-x] + 1 # for x           
    elif x1==x2:
        cor1 = y1
        cor2 = y2
        static = x1
        if cor1<cor2: # increment
            for x in range((cor2-cor1)+1): # +1 because the last index should also be affected
                    matrix[cor1+x][static] = matrix[cor1+x][static] + 1 # for y          
        else: # decrement
            for x in range((cor1-cor2)+1): # +1 because the last index should also be affected
                    matrix[cor1-x][static] = matrix[cor1-x][static] + 1 # for y
    else:
        #iterations = max( abs(x1-x2), abs(y1-y2)) # figuring out how many times we have to go
        while True:
            #print("diagnonal insert, x, y is:", x,y) # missing the last step
            matrix[x][y] = matrix[x][y] + 1 
            if x != x2:
                if x1<x2: x = x + 1
                elif x1>x2: x = x - 1
            if y != y2:
                if y1<y2: y = y + 1
                elif y1>y2: y = y - 1  
            if x==x2 and y==y2:
                #print("diagnonal insert, x, y is:", x,y)
                matrix[x][y] = matrix[x][y] + 1 # quick fix as to not skip a step
                break              
    #printM()
  
         
for cor in coordinate_pair:
    #print(cor)
    #print(cor['y2'])
    iterateMatrix(cor['x1'], cor['y1'], cor['x2'], cor['y2'])

printM()



'''
for x in range((abs(x2-x1))+1): # +1 because the last index should also be affected
        # Assuming x1-x2 is always the same as y1-y2, we only need to check whether or not y1-y2 is negative or positive.
        for y in range ((abs(y2-y1))+1):
            if x1<x2: # increment
                matrix[y1+y][x1+x] = matrix[y1+y][x1+x] + 1 # for x
            elif x1>x2:
                matrix[y1-y][x1-x] = matrix[y1-y][x1-x] + 1 # for x
            if y1<y2:
                matrix[x1+x][y1+y] = matrix[x1+x][y1+y] + 1
            elif y1>y2:
                matrix[x1-x][y1-y] = matrix[x1-x][y1-y] + 1 # for y
'''