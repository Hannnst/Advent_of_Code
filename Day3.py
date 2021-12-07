
bins = []
original1 = []
original = []
# each index of array bins contains all the numbers on a given index. 
with open("bin.txt", "r") as a_file:
  for line in a_file:
    binary = list(line.strip())
    original.append(binary)
    original1.append(binary)
    #print(binary)
    if len(bins) < 1:
        for i in range(len(binary)):
            bins.append([])
    for i in range(len(binary)):
        bins[i].append(binary[i])

def findDom(b, common):
    onec = 0
    zeroc = 0
    for bit in b:
        if bit == '0':
            zeroc = zeroc + 1
        elif bit == '1':
            onec = onec + 1
    if (common == True):
        return '1' if onec >= zeroc else '0' # OXY, most common
    return '0' if onec >= zeroc else '1' # CO2, least common

oxygen = []
co2 = []
index = 0
for b in bins:
    temp = []
    dom = findDom(b, True)
    print("dom is ", dom)
    for b in original:
        if b[index] == dom:
            temp.append(b)
    print(temp)
    original = temp
    index = index + 1
    if len(original) == 1:
        oxygen = original[0] # noe galt med oxy, får for lite tall?

index = 0
for b in bins:
    temp = []
    dom = findDom(b, False)
    for b in original1:
        if b[index] == dom:
            temp.append(b)
    original1 = temp
    index = index + 1
    if len(original1) == 1:
        co2 = original1[0]

print("CO2      scrubber rating is: ", co2)
print("Oxygen generation rating is: ", oxygen)

value1 = 0
for i in range(len(oxygen)):
	digit = oxygen.pop()
	if digit == '1':
		value1 = value1 + pow(2, i)
print("oxy: ", value1)
value = 0
for i in range(len(co2)):
	digit = co2.pop()
	if digit == '1':
		value = value + pow(2, i)
print("co2: ", value)
print("The life support rating is ", value1 * value)






