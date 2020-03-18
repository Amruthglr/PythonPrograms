number = input("Enter any serious od number with as many seperators as you like: \n")
seperators = ''

for i in number:
    if not i.isnumeric():
        seperators = seperators + i
print(seperators)

seperators2 = ""
for i in number:
    if i.isnumeric():
        seperators2 = seperators2 + i
print(seperators2)