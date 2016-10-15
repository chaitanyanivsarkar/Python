l=[12,14,5,64,79,52,476]
def display():
    print "list",l
def delete ():
    l.pop()
    print l
def add():
    a=input("enter the value to be added:")
    l.append(a)
def isempty():
    if l==[]:
        print "list is empoty"
    else:
        print "the list is not empty"
def peek():
    print l[len(l)-1]

display ()
delete ()
peek()
isempty()
add()
