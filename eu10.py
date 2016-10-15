n=input()
S=set(range(2,n))
l=[]
while S:
    x=S.pop()
    l.append(x)
    S.difference_update(set(range(2*x,n+1,x)))
print l[10000]
