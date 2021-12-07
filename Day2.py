

global depth
global horizontal
global aim

depth = 0
horizontal = 0
aim = 0

def forward(val):
    global horizontal
    global aim
    global depth
    
    horizontal = horizontal + val
    depth = depth + (aim * val)

def down(val):
    global aim
    aim = aim + val

def up(val):
    global aim
    aim = aim - val

def move(func, val):
    if func == 'forward':
        forward(val)
    elif func == 'down':
        down(val)
    elif func == 'up':
        up(val)

with open("directions.txt", "r") as a_file:
    for line in a_file:
        func, val = line.split(" ")
        move(func, int(val))
        print(func, " with value ", val)
print("depth: ", depth, ", position: ", horizontal)
print(depth*horizontal)



