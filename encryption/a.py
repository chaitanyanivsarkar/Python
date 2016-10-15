import string, random
f=file("tab.txt","w")
allchars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+string.whitespace
l=list(allchars)
table=[]
i=0
def randomise(l):
    lf=[]
    l1=[]
    n=len(l)
    m=0
    while m<n:
        j=random.randint(0,n-1)
        if str(j)+"," not in l1 and len(l1) <= 4*len(l):
            lf.append(l[j])
            l1.append("\'"+str(j)+"\'"+",")
            m+=1
    return lf
while i<len(l):
    l1=randomise(l)
    table.append(l1)
    i+=1
for i in range(len(l)):
    m=list("[")+table[i]+list("]")
    print m
    f.writelines(m)
    f.write("\n\n\n")
    f.flush() 
