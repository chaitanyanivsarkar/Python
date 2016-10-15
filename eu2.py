l=0
def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)
for i in range(1,12):
    l=l+fib(3*i)
print l
