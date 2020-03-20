#More on While Loops

Exits_available = ["East", "North", "South", "West"]

choosen_Exit = ""
while choosen_Exit not in Exits_available:
    choosen_Exit = input("Enter the where do you want to exit : ")

print("arent you glad you got out out ")