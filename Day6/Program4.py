# A python Program using a student class with instance methods to process the data of several students

class Students(object):
    def __init__(self, name , marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Student Name is {}".format(self.name))
        print("Student Marks is {}".format(self.marks))

    def ClaculateGrade(self):
        if self.marks > 90:
            print("Grade A")
        elif self.marks > 80:
            print("Grade B")
        elif self.marks > 70:
            print("Grade C")
        else:
            print("Fail")

stud = int(input("Enter the Number of students: "))

i = 0

while i < stud:
    StudentName = input("Enter the Student name: ")
    StudentMarks = int(input("Enter the Student Marks: "))
    Stud1 = Students(StudentName,StudentMarks)
    Stud1.display()
    Stud1.ClaculateGrade()
    i += 1

#Using Lists
# StudList = []
# while i < stud:
#     StudentName = input("Enter the Student name: ")
#     StudentMarks = int(input("Enter the Student Marks: "))
#     # Stud1 = Students(StudentName,StudentMarks)
#     # Stud1.display()
#     # Stud1.ClaculateGrade()
#     StudList.append(Students(StudentName,StudentMarks))
#     i += 1
# for i in StudList:
#     i.display()
#     i.ClaculateGrade()