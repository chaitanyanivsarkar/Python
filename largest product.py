def product(l):
    p = 1
    for i in l:
        p *= int(i)
    return p
a=raw_input()
l=[]
for i in range(len(a)-12):
    if "0" not in a[i:i+13]:
        x=list(a[i:i+13])
        l.append(x)
j,k=0,0
for i in range(len(l)):
    j=product(l[i])
    if j>k:
        k=j
print k
