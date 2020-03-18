#guess a number and ask for one more choise if it goes wrong

guess = 5

GuessNumber = int(input(" Guess a Number between 1-10 : "))

if GuessNumber == guess :
    print("you have guessed number correctly")
elif GuessNumber > guess :
    print("your guess is bit higher")
    GuessNumber = int(input("Try again buddy, Guess a number: "))
    if GuessNumber == guess :
        print("your guess is correct")
    else:
        print("its wrong again")
else:
    print("your guess is bit lower")
    GuessNumber = int(input("Try again buddy, Guess a number: "))
    if GuessNumber == guess:
        print("your guess is correct")
    else:
        print("its wrong again")

# different approach

if GuessNumber != guess:
    print("Your guess is incorrct ")
    if GuessNumber > guess:
        print("your number is bit higher")
    else:
        print("your number is bit lower")
    GuessNumber = int(input("Try again buddy, Guess a number: "))
    if GuessNumber == guess:
        print("your guess is correct ")
    else:
        print("your wrong again buddy")
else:
    print("your guess is correct ")