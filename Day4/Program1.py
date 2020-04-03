#List and its methods

players = ["Chinmay", "Sayali", "Pooja", "Reshma", "Pooja"]

print(players[1:])
print(players[0])
print(players[3:-1])
print(players[-4])
print('\n')
# Printing every element in the list

for i in players:
    print(i)
print('\n')
# changing the values of particular index

print("Before changing")
print(players)
print("After Changing")
players[1] = 'Amruth'
print(players)

# to verify weather the element is present in the list

element = 'Amruth'


if element in players:
    print("{} is in players ".format(element))
else:
     print("{} is not in players".format(element))

# Removing from list

players.remove('Sayali')
print(players)
x = players.pop(2)
print(x)

# Adding to list

players.append("Amruth")
print(players)

# Joining of two list
list1 = [1,2,4,5]
list2 = [10,20,30,40]

list3 = list1 + list2

print(list3)

for num in list2:
    list1.append(num)
print(list1)

list3.extend(list1)
print(list3)

list3.reverse()
print(list3)

list3.insert(3, 234534534)
print(list3)


