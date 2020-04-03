namelist = [
        {"name": "Chinmay", "Roll No": "89", "Age":27, "Skills":"JavaScript"},
        {"name": "Amruth", "Roll No": "82", "Age":24, "Skills":"Python"},
        {"name": "Sarika", "Roll No": "61", "Age":23, "Skills":"C++"},
        {"name": "Sayali", "Roll No": "72", "Age":26, "Skills":"Electron"},
        {"name": "Amit", "Roll No": "90", "Age":24, "Skills":"JavaScript"},
]

name  = input("Please Enter the name you want to search")

count = False

for dict in namelist:
    if dict.get("name") == name:
        count = True
        for keys,values in dict.items():
            print("{} : {}".format(keys,values))
        break

if count == False:
    print("Name is not vailable: \n try again ")
