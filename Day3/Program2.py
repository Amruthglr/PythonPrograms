# break Statement in Python

shopping_List = ["Milk", "Pasta", "Egg", "spam", "Bread", "Rice"]
count = 0
for item in shopping_List:
    if item != "spam":
        count += 1
    else:
        break
print(count)

# Different Approach

for item in range(len(shopping_List)):
    if shopping_List[item] == "spam":
        print("index of the spam is {}".format(item))
        break

different approach

if "spam" in shopping_List:
    print("the Index of spam is {}".format(shopping_List.index("spam")))
