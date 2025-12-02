allLines = []
diagram = []
max_coor = 0
def makeDiagram(cfrom, cto):
    ''' x, y = crom[0], cfrom[1] '''
    #for line in diagram:
        #print(line)
    #print("MakeDiagram called with from, to, values: ", cfrom, cto)
    fromx, fromy = int(cfrom[0]), int(cfrom[2]) # index 2 was a comma so we skip that
    tox, toy = int(cto[0]), int(cto[2]) # index 2 was a comma so we skip that
    print("values to be iterated over: ", fromx, fromy, ",", tox, toy)
    ''' Count coordinates from, and to, the given coordinates and change the value accordingly '''
    # SHould just do linear horizontal lines for part 1:
    if fromx == tox:
        while fromy != toy: # have to count down or up to reach from-to
            print("FROMY: ", fromy)
            print("diagram[x][y] is ", diagram[fromx][fromy])
            if diagram[fromx][fromy] == '.': diagram[fromx][fromy] = 1
            else: diagram[fromx][fromy] = diagram[fromx][fromy] + 2
            if fromy < toy: fromy = fromy + 1
            elif fromy > toy: fromy = fromy - 1

    elif fromy == toy:
        while fromx != tox: # have to count down or up to reach from-to
            print("FROMX: ", fromx, "TOX:", tox)
            print("diagram[x][y] is ", diagram[0][9])
            if diagram[fromx][fromy] == '.': diagram[fromx][fromy] = 1
            else: diagram[fromx][fromy] = diagram[fromx][fromy] + 1
            if fromx < tox: fromx = fromx + 1
            elif fromx > tox: fromx = fromx - 1
            

            

with open("Files/day5_test.txt", "r") as a_file:
    for line in a_file:
        data = line.strip().replace(" ", "").split('->')
        print(data)
        allLines.append(data)

#create empty diagram
max_coor = int(max(max(max(allLines)))) # find the largest number so we find wdith and length of diagram
for x in range(max_coor+1):
    line = []
    for y in range(max_coor+1):
        line.append('.')
    diagram.append(line)

# Fill diagram with points
for data in allLines:
    print("new iteration")
    coor_from = data[0] # 0,9
    coor_to = data[1] # 0,9
    makeDiagram(coor_from, coor_to)

for line in diagram:
    print(line)


