Binary file handelling
import pickle
class Student:
    def __init__(self,name="",roll=0):
        self.rollno=roll
        self.name=name
        self.mark1,self.mark2,self.mark3=0.0,0.0,0.0
    def readmarks(self):
        self.mark1=float(raw_input("enter marks"))
        self.mark2=float(raw_input("enter marks"))
        self.mark3=float(raw_input("enter marks"))
    def display(self):
        print "student detail"
        print "roll no =",self.rollno
        print "name of student",self.name
        print self.mark1,self.mark2,self.mark3
stud1=Student(13,"rohan")
stud2=Student(15,"nitya")
stud1.readmarks()
stud2.readmarks()
f=open("E:\\student2.txt","wb")
pickle.dump(stud1,f)
pickle.dump(stud2,f)
f.close()
         

