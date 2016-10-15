Counting vovels
x=0
a=raw_input("enter a string")
b='aeiouAEIOU'
for i in range (0,len(a)):
    if a[i] in b :
        x+=1
print "the no of vovels is",x
