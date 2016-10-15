class Library_books :
    no_of_books=0
    def __init__(self):
        self.name=""
        self.genere=""
        self.type1=""
        self.desc=""
        self.shelf_no=""
    def addition_of_books(self):
        Library_books.no_of_books+=1
        self.name=raw_input("enter the name of the book : ")
        self.genere=raw_input("enter the genere of the book : ")
        self.type1=raw_input("enter the type of the book (I/NI) : ")
        self.desc=raw_input("enter the desceription of the book : ")
        self.shelf_no=raw_input("enter the shelf number of the book : ")
        self.f=file("D:\\chaitanya\\tabelofbooks.xls","a+")
        self.f.write("\n")
        self.f.write(str(Library_books.no_of_books))
        self.f.write("\t")
        self.f.write(self.name)
        self.f.write("\t")
        self.f.write(self.genere)
        self.f.write("\t")
        self.f.write(self.type1)
        self.f.write("\t")
        self.f.write(self.desc)
        self.f.write("\t")
        self.f.write(self.shelf_no)
        self.f.close()
    def issue_of_books(self):
        self.f=file("D:\\chaitanya\\tabelofbooks.xls","a+")
        self.name=raw_input("enter the name of the book : ")
        a=self.f.read()
        b=a.find(self.name)
        c=self.f.read(b+len(self.name)+len(self.genere)+len(self.type1)+len(self.desc)+len(self.shelf_no))
        self.f.write("\t")
        self.f.write("N/A")
obj=Library_books()
obj.addition_of_books()
obj.issue_of_books()
                 



