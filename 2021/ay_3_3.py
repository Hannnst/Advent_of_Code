
input = []
with open("binf.txt", "r") as a_file:
  for line in a_file:
      input.append(line.strip())

O2=input
CO2=input
pos=0
while len(O2)>1:
    
    amount=0
    for i in O2:
        if i[pos]=='1':
            amount=amount+1
    if amount*2>=len(O2):
        MC='1'#1 most common
    else:
        MC='0'#0 most common
    O2 = list(filter(lambda x:x[pos]==MC,O2))
    
    pos = pos+1
print(O2)  
pos=0
while len(CO2)>1:
    
    amount=0
    for i in CO2:
        if i[pos]=='1':
            amount=amount+1
    if amount*2<len(CO2):
        MC='1'#1 least common
    else:
        MC='0'#0 least common
    CO2 = list(filter(lambda x:x[pos]==MC,CO2))
    
    pos = pos+1
print(CO2)  

print(int(O2[0],2)*int(CO2[0],2))