''' Script that finds lack of different closed parantheses

Example line: {([(<{}[<>[]}>{[]{[(<()>

could count amount of ( vs ) and the same for the others.

'''
# Lists with the possible symbols, in this case left and right parantheses
# symbol : count


lines = []
with open("Files/day10.txt", "r") as f:
  for line in f:
    temp = []
    for symbol in line.strip():
        temp.append(symbol)
    lines.append(temp)

# code that doesn't do entirely what it should, i misunderstood the task a little
'''syntaxErrorScore = 0
symbolValues = { ')':3, ']':57,'}':1197,'>':25137 }
for l in lines:
    lefts = {'[':0,'(':0,'<':0,'{':0}
    rights = {']':0,')':0,'>':0,'{':0}
    for symbol in l:
        for k in lefts.keys():
            if symbol == k:
                lefts[k] += 1
        for k in rights.keys():
            if symbol == k:
                rights[k] += 1
    # calculate sum here
    print("score on line: ", lefts, rights)

    for left, right in zip(lefts.keys(), rights.keys()):
        if lefts[left] != rights[right]:
            syntaxErrorScore += abs(lefts[left]-rights[right]) * symbolValues[right]

print("SyntaxError score is", syntaxErrorScore)'''

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

match = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<'
}

okay = []
score = 0
for line in lines:
    stack = []
    good = True
    for c in line:
        if c in '([{<':
            stack.append(c)
        else:
            if match[c] != stack.pop():
                score += points[c]
                good = False
                break
    if good:
        okay.append(stack)

print("The syntax error score is ", score)

points = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4
}

# part 2
'''
Find the completion string for each incomplete line, score the completion strings,
and sort the scores. What is the middle score?
'''
scores = []
for end in okay:
    end.reverse()
    score = 0
    for el in end:
        score *= 5
        score += points[el]
    scores.append(score)

scores.sort()
print("The middle score of incomplete lines is ", scores[len(scores)//2])


