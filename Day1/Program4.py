# get input to guess a no and tell him if it is lowe ror higher

answer = 5

Guess = int(input("Guess the number between 1-10: "))
if Guess == 5:
    print("you have guessed the correct number")
elif Guess > 5:
    print("you should have guess lower number ")
else:
    print("you should have guess higher number")