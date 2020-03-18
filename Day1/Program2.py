age = int(input("Enter your AGE: "))

if age > 18 :
    print("You are eligible to vote")
    print("vote for your favourite candidate")
else:
    print("You still need to wait for {} years".format(18-age))

# Another way to write
if age < 18:
    print(f"You nedd still wait for {18-age} years")
else:
    print("your eligible to vote")
