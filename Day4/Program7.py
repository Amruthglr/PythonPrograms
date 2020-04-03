# quiz with Dict

questions = {
            "What is the Capital of Maharastra" : "Mumbai",
            "What is the Capital of Kharnataka" : "Bengaluru",
            "What is the Capital of TamilNadu"  : "Chennai"
}

count = 0
for qns, ans in questions.items():
    userinput = input(qns)
    if userinput == ans:
        count += 1

if count == 3:
    print("Gold")
elif count == 2:
    print("Silver")
elif count == 1:
    print("Bronze")