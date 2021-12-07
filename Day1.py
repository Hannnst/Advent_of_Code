measurements = []
increased = 0
groups = []

''' Script that calculates how many numbers appear increased for each iteration from a list '''
with open("Files/day1.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    measurements.append(stripped_line)

for i in range(len(measurements)-3):
    groups.append(int(measurements[i])+int(measurements[i+1])+int(measurements[i+2]))

for i in range(len(groups)-1):
    if groups[i] < groups[i+1]:
        increased = increased + 1

print(increased)



