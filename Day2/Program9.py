#and or operator in python

age = int(input("Enter your age: "))

if age >18 and age <65:
    print("Have a good day at work")
else:
    print("Enjoy your life")

# another way of writing

if 18 <= age <=65:
    print("have a good day at work")
else:
    print("ENjoy your golden days")

print('--'*80)

if age > 18 or age <65:
    print("have a good day at work")
else:
    print("enjoy")

