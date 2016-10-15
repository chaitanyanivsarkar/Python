def swarpelement(alist):
    i=0
    while (i<len(alist)-1):
        if (alist[i]>alist[i+1]):
            temp=alist[i]
            alist[i]=alist[i+1]
            alist[i+1]=temp
        i=i+1
        print "list after pass",(i),":",alist
def bubblessort(alist):
    for num in range(len(alist)-1):
        swarpelement(alist)
l=[15,14,25,64,79,56]
print "original list is:",l
bubblessort(l)
print "list after sorting :",l 
                
            











