DomainFile= "input.txt"
list=[]
file = open(DomainFile, "r")
for line in file:

   list.append(line)


for i in list:
    print(i)


list.insert(0,"Some New Domain")

print("Printing the list of dimains again to check if the domain has been inserted at the 0th index")

for i in list:
    print(i)


