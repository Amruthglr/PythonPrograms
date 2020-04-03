#dictionary

dictionaryname = {
            "name" : "Amruth",
            "age" : 25,
            "Roll No" : 10,
            "Is Married" : True
}

print(dictionaryname["age"])

for abc in dictionaryname:
    print("{} and {} ".format(abc,dictionaryname[abc]))

for abc in dictionaryname.keys():
    print(abc)

for abc in dictionaryname.values():
    print(abc)

for keys, values in dictionaryname.items():
    print("{} : {}".format(keys,values))