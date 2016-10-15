def insertionsort(AR):
    for i in range(1,len(AR)):
        v=AR[i]
        j=i
        while AR[j-1]>v and j>=1:
            AR[j]=AR[j-1]
            j=-1
        AR[j]=v
l=[12,45,75,74,64]
print "original list",l
insertionsort(l)
print "list after sorting:",l
