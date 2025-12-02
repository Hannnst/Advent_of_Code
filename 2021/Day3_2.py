binary_numbers = []
binary_numbers_per_index = []
dominant_per_index = []

with open("Files/day3.txt", "r") as a_file:
  for line in a_file:
      binary_numbers.append(list(line.strip()))
      for b in range(len(line.strip().split())):
        binary_numbers_per_index.append([]) # initiate the array for all indexes
        dominant_per_index.append([]) # initiate the array for all indexes

def populateBinaryPerIndex():
    for binary_number in binary_numbers:
        index = 0
        for number in binary_number:
            binary_numbers_per_index[index].append(number)
            #print(binary_numbers_per_index)
            index = index + 1

def populateDomPerIndex(common):
    onec = 0
    zeroc = 0
    index = 0

    print(binary_numbers_per_index)
    for indexes in binary_numbers_per_index:
        for bit in indexes:
            if bit == '0':
                zeroc = zeroc + 1
            elif bit == '1':
                onec = onec + 1
        #print(" ones are ", onec, "zeros are ", zeroc)
        if (common == True):
            if onec >= zeroc:
                dominant_per_index[index] = '1'
            else:
                dominant_per_index[index] = '0'
        else:
            if onec >= zeroc:
                dominant_per_index[index] = '0'
            else:
                dominant_per_index[index] = '1'
        index = index + 1
        

populateBinaryPerIndex()
print(binary_numbers_per_index)
populateDomPerIndex(True)
print(dominant_per_index)


