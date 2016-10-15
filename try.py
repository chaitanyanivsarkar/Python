import pickle
class Student:
    def __init__(self,name="",roll=0):
        self.rollno=roll
        self.name=name
        self.mark1,self.mark2,self.mark3=0.0,0.0,0.0
    def readmarks(self):
        print("enter marks")
        self.mark1=float(raw_input("enter marks"))
        self.mark2=float(raw_input("enter marks"))
        self.mark3=float(raw_input("enter marks"))
    def display(self):
        print("student detail")
        print("roll no =",self.rollno)
        print("name of student",self.name)
        print(self.mark1,self.mark2,self.mark3)
stud1=Student(13,"rohan")
stud1.readmarks()
file1=open("student2.txt","rb")
try:
    while True:
        stud1=pickle.load(file1)
        stud1.display()
except EOFError:
    file1.close()