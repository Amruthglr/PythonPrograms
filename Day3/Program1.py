#continue Statement

shopping_list = ["milk", "Pasta", "Eggs", "Spam", "Bread", "Rice"]

# for item in shopping_list:
#     if item != "Spam":
#         print("Buy", item)

for item in shopping_list:
    if item == "Spam":
        continue
    else:
        print("Buy",item)