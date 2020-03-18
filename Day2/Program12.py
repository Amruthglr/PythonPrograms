parrot = "Norwegian Blue"

letter = input("Enter a letter : ")

if letter in parrot:
    print("{} in {}".format(letter,parrot))
else:
    print("I dont need that letter")