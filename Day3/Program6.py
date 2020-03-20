#with continue and without continue

for i in range(21):
    if i % 3 == 0 or i % 5 == 0:
        continue
    else:
        print(i)

# without continue
for i in range(21):
    if i % 3 != 0 and i % 5 != 0:
        print(i)