import bisect
l=[10,20,30,40,50,60,70]
print "the list is "
print l
ITEM=int(input("enter the new element :"))
ind=bisect.bisect(l,ITEM)
bisect.insort(l,ITEM)
print ITEM ,"insert at index",ind
print "the list after inserting new element is "
print l
