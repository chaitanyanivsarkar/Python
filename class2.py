Use of class variable
''' USE OF CLASS VARIABLE'''
class Student:
    no_of_student=0
    calssteacher="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks
        self.grade=""
        Student.no_of_student+=1
    def calcofgrade(self):
        if self.marks>=90:
            self.grade="A+"
        elif self.marks>=80 and  self.marks<90:
            self.grade="A"
        elif self.marks>=70 and  self.marks<80:
            self.grade="B"
        elif self.marks>=60 and  self.marks<70:
            self.grade="C"
        elif self.marks>=50 and  self.marks<60:
            self.grade="D"
        elif self.marks>=40 and  self.marks<50:
            self.grade="E"
        elif self.marks>=0 and  self.marks<40:
            self.grade="F"
    def display(self):
        print "name : ",self.name
        print "rollno : ",self.roll
        print "marks : ",self.marks
        print "grade : ",self.grade
        print "____________________________________________________________________________________________________________________________________________"
for x in range(4):
    a,b,c=input("enter the rollno : "),raw_input("enter the name : "),input("enter the marks : ")
    s1=Student(a,b,c)
    s1.calcofgrade()
    s1.display()
print Student.no_of_student
print Student.calssteacher
