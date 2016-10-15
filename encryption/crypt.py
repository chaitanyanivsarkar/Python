import thread, string, rand
allchars=string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation+string.whitespace
l=list(allchars)
l.sort()
table=[]
def Keygen(key, org):
    #making the key as long as the orignal text
    m=""
    l=list(key)
    for i in range(len(org)):
        m = m + l[i%len(l)]
    key = m
    return key
def Cipher():
    #implementing the one time pad
    table=[]
    i=0
    while i<len(l):
        l1=rand.randomise(l)
        table.append(l1)
        i+=1
    return table
def encrypt(org,key,table):
    out=""
    i=0
    n=len(org)
    while i<n:
        a=l.index(org[i])
        b=l.index(key[i])
        out=out+table[b][a]
        i+=1
    return out
def write(out):
    f=file("encryptedtext.txt","w")
    f.write(out)
    f.close()
    rand.tabwrite()
f=file("a.txt","r")
org=f.read()
key=raw_input("enter the password: ")
k=Keygen(key,org)
table=Cipher()
out=encrypt(org,k,table)
write(out)
