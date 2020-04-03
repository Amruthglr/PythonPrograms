# Small Quiz

questions = ['What is the capital of MH', 'What is the capital of KA', 'What is the capital of TN']

answers = ['Mumbai', 'Bangalore', 'Chennai']

user_ans = []
count = 0

while count < len(questions):
    answer = input(questions[count])
    user_ans.append(answer)
    count +=1

count = 0
for item in range(len(user_ans)):
    if answers[item] == user_ans[item]:
        count += 1

if count == len(answers):
    print("Gold")
elif count ==2 :
    print("Silver")
elif count == 1 :
    print('bronze')
else:
    print("You got it all Wrong")


