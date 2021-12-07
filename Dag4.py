bingos = [83,5,71,61,88,55,95,6,0,97,20,16,27,7,79,25,81,29,22,52,43,21,53,59,99,18,35,96,51,93,14,77,15,3,57,28,58,17,50,32,74,63,76,84,65,9,62,67,48,12,8,68,31,19,36,85,98,30,91,89,66,80,75,47,4,23,60,70,87,90,13,38,56,34,46,24,41,92,37,49,73,10,94,26,42,40,33,54,86,82,72,39,2,45,78,11,1,44,69,64]
#bingos = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
boards= []
found_numbers = []

'''
example of board:
97 62 17  5 79
 1 99 98 80 84
44 16  2 40 94
68 95 49 32  8
38 35 23 89  3

possible solution: each board is a 2d array.
After 5 numbers are fetched, check possible numbers - for each x, check all x and y's and check if 
the numbers on the same x and y axis is also mentioned in the found numbers array.

When all numbers on either x values or y values are found in the foundnumbers array, the board has won!

One function for checking all y and x from given number must be made.
'''

# creating boards
with open("bingo.txt", "r") as a_file:
    temp = []
    for line in a_file:
      if line == '\n':
          boards.append(temp)
          temp = []
      else:
          temp.append(list(line.strip().split()))
board_x = len(boards[0])
board_y = len(boards[0][0])

for i in range(len(boards)):
    found_numbers.append([]) # each array represent found numbers in each board

#print("ALL BOARDS:")
#for board in boards:
#    print(board)


def calculateScore(boardNr, curBoard, fetchedNumber):
    '''finding the sum of all unmarked numbers on that board
    Multiply it by the fetched number'''
    print("fetchedNumber:", fetchedNumber)
    print("found numbers for board is ",found_numbers[boardNr] )
    
    sum = 0
    for line in curBoard:
        for number in line:
            if number not in found_numbers[boardNr]:
                print("number not found is ", number)
                sum = sum + int(number)
    
    return sum * int(fetchedNumber)

def checkBingo(boardNr, xp,  yp):
    '''A number is found and method checks if all numbers on horizontal or diagonal line is part of the
    currently found numbers of the given board'''
    # remove 1 to correspond to array logic
    x = xp-1
    y = yp-1
    bingoLine = []
    curBoard = boards[boardNr]
    fetchedNumber = curBoard[x][y]
    for xb in range(board_x):
        #print("checks curBoard x, xb val: ", x, xb)
        if curBoard[x][xb] in found_numbers[boardNr]:
            print("checks number:", curBoard[x][xb])
            bingoLine.append(curBoard[x][xb])
        else: # x values not bingo, check y values
            bingoLine = []
            for yb in range(board_y):
                if curBoard[yb][y] in found_numbers[boardNr]:
                    bingoLine.append(curBoard[yb][y]) # saves the numbers and erases them depending on how far they get
                else:
                    bingoLine = []
                    return False
    print("\n\nBINGO!\n Found: ", bingoLine , "\n On board: " )
    for line in boards[boardNr]:
        print(line)
    print("\n Score is: ", calculateScore(boardNr, curBoard, fetchedNumber))
    return True # returns true if False is not returned earlier

# Fetching numbers
winner = False
while len(bingos) > 0:
    bingo_number = bingos.pop(0)
    print("fetched number ", bingo_number)
    board_count = 0
    for board in boards:
        #print("checks board ", board)
        x = 0
        for lines in board:
            y = 0
            x = x + 1
            for number in lines:
                y = y + 1
                if int(number) == int(bingo_number):
                    print("Found match: ", number, " == ", bingo_number ,"on coordinates [", y, ",", x, "]", "on board ", board_count) # x, y coor has switched somehow.
                    found_numbers[board_count].append(number) # bingo number found
                    # check all coordinates up and dowwn from here before going further to check for winners?
                    winner = checkBingo(board_count, x, y) # x, y coor of the found number will help us
                    if winner == True:
                        #exit(0) # for part 1, when we want to win
                        pass # when we want to find the last board that wins
        board_count = board_count + 1





