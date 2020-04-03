# random function and FLag

import random

machineno = random.randint(1,10)
userinput = int(input("Guess a number between 1 - 10 : "))
correctGuess = False
count = 0

if userinput != machineno:
    if userinput > machineno:
        print("guess lower number")

    else:
        print("Guess higher number")

    userinput = int(input("Guess a number between 1 - 10 : "))

    if userinput == machineno:
        correctGuess = True
else:
    correctGuess = True

if correctGuess:
    print("you have guessed it correct")
else:
    print("You have guessed it wrong ")