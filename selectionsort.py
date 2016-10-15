def selection_sort(list):
    i=0
    for curpos in range (len(l)):
        minpos=curpos
        for scanpos in range(curpos+1,len(l)):
                        if (l[scanpos]<l[minpos]):
                            minpos=scanpos
                        temp=l[minpos]
                        l[minpos]=l[curpos]
                        l[curpos]=temp
                        i=i+1
                        print "list after pass",(i),":",l
l=[10,51,20,46,31]
print"original list is",l
selection_sort(l)
print l
