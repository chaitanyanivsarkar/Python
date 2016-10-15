import random, csv
x=[]
def randomise(l):
    lf=[]
    l1=[]
    n=len(l)
    m=0
    while m<n:
        j=random.randint(0,n-1)
        if str(j)+"," not in l1 and len(l1) <= len(l):
            lf.append(l[j])
            l1.append(str(j))
            m+=1
    x.extend(l1)
    return lf
def tabwrite():
    with open("tab.csv","wb") as csvfile:
        y=csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        y.writerow(x)
    csvfile.close()
