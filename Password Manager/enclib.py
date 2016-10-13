import random,string
def stringshuffle(x):
        x=list(x)
        i=len(x)-1
        while i>0:
                y=random.randint(0,741852)%(i+1)
                a=x[y]
                x[y]=x[i]
                x[i]=a
                i-=1
        return x
def table():
        f=file("tab.pmc","w")
        c=string.printable
        pad=[]
        for i in range(len(c)):
                y=stringshuffle(c)
                f.writelines(y)
                f.write("\n\n\n")
def encrypt(x,y):
        f=file("tab.pmc","r+")
        c1=f.read()
        tab=[]
        i=0
        while i<len(c1):
            j=i+100
            tab.append(list(c1[i:j]))
            i=j+3
        f.close()
        del c1
        del f
        del i
        c=string.printable
        a,z="",""
        for i in range(len(x)):
                j=i%len(y)
                a=a+y[j]
        y=a
        for i in range(len(x)):
                m=c.find(x[i])
                n=c.find(y[i])
                z=z+tab[n][m]
        return z
def decrypt(x,y):
        f=file("tab.pmc","r+")
        c1=f.read()
        tab=[]
        i=0
        while i<len(c1):
            j=i+100
            tab.append(list(c1[i:j]))
            i=j+3
        f.close()
        del c1
        del f
        del i
        c=string.printable
        a,z="",""
        for i in range(len(x)):
                j=i%len(y)
                a=a+y[j]
        y=a
        del a
        for i in range(len(x)):
                n=c.find(y[i])
                d="".join(tab[n])
                m=d.find(x[i])
                z=z+c[m]
        del m
        del n
        return z
