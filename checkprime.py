def checkprime(a):
	i,b=3,int(a**(1/2))
	if a==2 :
		return True
	elif a%2==0 and a!=2:
		return False
	j=True
	elif a%2!=0 :
		while i<b+1:
			if a%i==0:
				j=False
				return j
				break
			i+=2
def check(a):
	j=True
	if ((2**a)-2)%a !=0:
		j=False
	return j
a=int(input())
print(checkprime(a))
a=input()
