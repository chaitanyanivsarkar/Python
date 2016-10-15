l=[10,11,12,13,14,15,45]
m=0
a=input("enter the element you want to found")
i,b=len(l)-1,0
while  b<=l:
    m=(b+i)/2
    if l[m]==a:
        print "finish"
        print a,"found",m
        break
    elif l[m]<a:
        b=m+1
    elif l[m]>a:
        i=m-1
    elif b!=i:
        print "not found"
        break
