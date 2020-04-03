# Random module
# ask the user to guess the no

import random
machinenum = random.randint(1,10)

#how many trials

i = 1

while i < 6 :
    userinput = int(input("Enter a num between 1 - 10 : "))
    if userinput == machinenum:
        print("your guess is correct")
        print(userinput)
        break
    i += 1
else:
    print("wrong guess")
