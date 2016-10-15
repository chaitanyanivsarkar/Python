import math
n=input()
l=1
for i in range(2,n):
    a=int(math.log(n,i))
    b=math.pow(i,a)
    if l%b!=0:
        l=l*b
    print b,a,i,l
print l
