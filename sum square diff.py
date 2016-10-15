def sumsq(n):
    l=n*(n+1)*(2*n+1)/6
    return l
def sqsum(n):
    l=(n*(n+1)/2)**2
    return l
print sumsq(100)-sqsum(100)
