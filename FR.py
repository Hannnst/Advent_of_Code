measurements = []
increased = 0
groups = []
with open("measurements.txt", "r") as a_file:
  for line in a_file:
    stripped_line = line.strip()
    measurements.append(stripped_line)

for i in range(len(measurements)-3):
    groups.append(int(measurements[i])+int(measurements[i+1])+int(measurements[i+2]))

for i in range(len(groups)-1):
    if groups[i] < groups[i+1]:
        increased = increased + 1

print(increased)



