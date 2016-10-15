class Person(object):
    def __init__(self,name="",age=0):
        self.name=name
        self.age=age
    def __str__(self):
        return self.name+" is "+str(self.age)+" years old"
class Student(Person):
    def __init__ (self,roll,clas,name,age):
        Person.__init__(self,name,age)
        self.rollno=roll
        self.clas=clas
    def __str__(self):
        string=self.name+" is "+str(self.age)+" years old and studies in class "+str(self.clas)+" and has roll no "+ str(self.rollno)
        return string
p=Person("Chaitanya",17)
s=Student(101,12,"Chaitanya",17)
print(p)
print(s)
a=input()
