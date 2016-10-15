def Bserch(AR,ITEM) :
     beg=0
     last=len(AR)-1
     while beg<=last:
         mid =(beg+last)/2
         if (ITEM==AR[mid]):
             return mid
         elif (ITEM > AR[mid]):
             beg=mid+1
         else :
             last=mid-1
     else:
        return False
l=[12,14,15,18,24,34]
print l
ITEM=int(raw_input("enter the element to be deleted:"))
position=Bserch(l,ITEM)
if position:
    del l[position]
    print l
else:
    print "sorry"
