# A Python Program to UnderStand Instance variable

class Student:

    def __init__(self,name ='', age=0, marks=0):
        self.firstname = name
        self.age = age
        self.marks = marks

sayali = Student('Sayali', 25, 90)
print(sayali.firstname)
print(sayali.age)
print(sayali.marks)

print("\n")

amruth = Student()
print(amruth.firstname)
print(amruth.age)
print(amruth.marks)

print("\n")

amruth = Student('Shiju')
print(amruth.firstname)
print(amruth.age)
print(amruth.marks)