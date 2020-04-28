#A program to store data into instance using mutator methods
#and tp retrive data from the instance using accessor methods

#getattr() method is called accessor classmethod
# setattr() method is called mutator

class Student(object):

    def setnamemarks(self,name,marks):
        self.name = name
        self.marks = marks

    def caluculategrade(self):
        if self.marks > 90:
            print("Grade A")
        elif self.marks > 80:
            print("Grade B")
        elif self.marks > 70:
            print("Grade C")
        else:
            print("Fail")

    def display(self):
        print("Student name {}".format(self.name))
        print("Student marks {}".format(self.marks))

stud = int(input("Enter the number of students: "))
# i = 0
# while i < stud:
#     studentname = input("Enter your Student name: ")
#     studentmarks = int(input("ENter the marks of student: "))
#     stud1 = Student()
#     stud1.setnamemarks(studentname,studentmarks)
#     stud1.display()
#     stud1.caluculategrade()
#     i += 1

#using Lists

i = 0
StudentList = []

while i < stud:
    studentname = input("ENter Student name: ")
    studentmarks = int(input("Enter the Student marks: "))
    StudentList[i] = Student()
    StudentList = StudentList[i].setnamemarks(studentname,studentmarks)
    i += 1

for i in StudentList:
    i.display()
    i.caluculategrade()