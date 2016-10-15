def prime_factor(n):
    l=[]
    i=2
    m=n
    while i<=m/i:
        if n%i==0:
            while n%i==0:
                n=n/i
            l.append(i)
        i+=1
    return l
print prime_factor(600851475143)[-1]
