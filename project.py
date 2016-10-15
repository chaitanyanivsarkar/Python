'''Library Management System'''
import os
f2=file("d:\\chaitanya\\members.xls","a+")
f1=file("d:\\chaitanya\\temp.xls","a+")
f3=file("d:\\chaitanya\\temp2.xls","a+")
f=file("d:\\chaitanya\\books.xls","a+")
class Books():
    no_of_books=0
    def __init__(self):
        self.title=""
        self.writer=""
        self.genere=""
        self.avaliblity=""
        self.ib=""
    def addition_of_book(self,t,w,g,a):
        Books.no_of_books+=1
        self.title=t
        self.writer=w
        self.genere=g
        self.avaliblity=a
        self.ib=""
        list1=["\n"+str(Books.no_of_books)+"\t"+self.title+"\t"+self.writer+"\t"+self.genere+"\t"+self.avaliblity+"\t"+self.ib]
        f.writelines(list1)
        f.flush()
    def search(self,i):
        a2=f.read()
        for l in range (len(a2)):
            if a2[l]==i:
                f.seek(l)
        print f.readline()
    def issue(self,i,j):
        a2=f.read()
        for k in range (len(a2)):
            if a2[k]==i:
                f.seek(k)
            else :
                continue
        m=f.readline()
        y=m.find(" A ")
        count=0
        f.seek(0,0)
        while f.readline():
            count+=1
            if count==int(i):
                f1.write(f.read(y-1))
                f1.write("\t")
                f1.write(" N ")
                f1.write("\t")
                f1.write(j)
            else :
                f1.write(f.readline())
        f.close()
        f1.close()
        os.remove("d:\\chaitanya\\books.xls")
        os.rename("d:\\chaitanya\\temp.xls","d:\\chaitanya\\books.xls")
class Members():
    def __init__(self):
        Members.no_of_members=0
        self.name=""
        self.address=""  
    def addition_of_member(self,n,a):
        Members.no_of_members+=1
        self.name=n
        self.address=a
        list1=["\n"+str(Members.no_of_members)+"\t"+self.name+"\t"+self.address]
        f2.writelines(list1)
    def deletion_of_members(self,i):
        a=f2.read()
        for k in range (len(a2)):
            if a2[k]==i:
                f.seek(k)
            else :
                continue
        f2.seek(x)
        m=f2.readline()
        count=0
        f2.seek(0,0)
        while f2.readline():
            count+=1
            if count==int(i):
                continue
            else :
                f3.write(f2.readline())
        f2.close()
        f3.close()
        os.remove("d:\\chaitanya\\members.xls")
        os.rename("d:\\chaitanya\\temp2.xls","d:\\chaitanya\\members.xls")
def menu():
    print '''press 1 for addition of books
    press 2 for addition of members
    press 3 for issueing of books
    press 4 for search
    press 5 for deletion of members'''
menu()
a=input("enter your choice: ")
if a==1 :
    b=raw_input("enter password: ")
    if b=="abcd":
        book=Books()
        x1=raw_input("enter the name of book: ")
        x2=raw_input("enter the name of writer: ")
        x3=raw_input("enter the genere: ")
        book.addition_of_book(x1,x2,x3," A ")
    else :
        print "access denied"
elif a==2 :
    b=raw_input("enter password: ")
    if b=="abcd":
        member=Members()
        x1=raw_input("enter the name of member: ")
        x2=raw_input("enter the address: ")
        member.addition_of_member(x1,x2)
    else :
        print "access denied"
elif a==3 :
    b=raw_input("enter name: ")
    if b in f2.read():
            book=Books()
            x1=raw_input("enter the ID of book: ")
            book.issue(x1,b)
    else :
        print "access denied"
elif a==4 :
    b=raw_input("enter name: ")
    if b in f2.read():
        book=Books()
        x1=raw_input("enter the title of book:- ")
        book.search(x1)
    else :
        print "access denied"
elif a==5 :
    b=raw_input("enter password: ")
    if b=="abcd":
        member=Members()
        x1=raw_input("enter the member Id ")
        member.deletion_of_member(x1,x2)
    else :
        print "access denied"
