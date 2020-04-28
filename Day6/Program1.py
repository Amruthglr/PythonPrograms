# a Python program to define student class and object to it, we will call the method and display details

# student age, marks, variables
#talk Method
#intialize the values


class Student:

    #Constructor
    def __init__(self,name,age,marks):
        self.studentname = name
        self.studentage = age
        self.studentmarks = marks
    #Method
    def talk(self):
        print("My name is {}".format(self.studentname))
        print("My age is {}".format(self.studentage))
        print("My marks is {}".format(self.studentmarks))

Amruth = Student("Amruth", 25, 450)
Amruth.talk()
print(Amruth.studentage)
# 2 types of method call
Student.talk(Amruth)
Amruth.talk()

# creating Object through List

StudentDetail = [Student("Amruth", 25, 450),Student("Bikesh", 27, 440),Student("Shashank", 29, 430),Student("Shiju", 23, 280),Student("Amar", 26, 445)]
StudentDetail[0].talk()
StudentDetail[3].talk()

for i in StudentDetail:
    i.talk()
    print("\n")
    Student.talk(i)

for i in range(len(StudentDetail)):
    Student.talk(StudentDetail[i])
    print("\n")
    StudentDetail[i].talk()