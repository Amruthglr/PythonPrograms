# count the unique items in the list

students = ['Sarika', 'Pooja', 'Amit', 'Sayali', 'Pooj', 'Amit','Pratiksha']

studentlist = []

for evystd in students:
    if evystd not in studentlist:
        studentlist.append(evystd)

print(studentlist)

# counting how many time it has been repeated
for evystd in studentlist:
    print("{}  is  --> {}".format(evystd, students.count(evystd)))

