def traverse(AR):
    size=len(AR)
    for i in range(size):
        print AR[i]
AR=[1,2,3,4,5,6,7,8,9,0]
size=int(raw_input("enter the size of linear list"))
AR[0]*size
print "enter element for the linear list"
for i in range(size):
    AR[i]=input("element",str(i),":")
print "traversing the list:"
traverse(AR)
