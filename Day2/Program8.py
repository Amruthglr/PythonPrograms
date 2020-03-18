#using

guess = 5

GuessNumber = int(input("Guess the Number: "))

if guess == GuessNumber:
    print("YOu have Guessed it correct")
else:
    if GuessNumber > guess:
        print("guess is bit high")
        GuessNumber = int(input("Guess a number: "))
        if GuessNumber == guess:
            print('you have gussed it correctly')
        else:
            print("you are wrong again")
    else:
        print("guess is bit low")
        guess = int(input("Guess a number: "))
        if GuessNumber == guess:
            print('you have gussed it correctly')
        else:
            print("you are wrong again")