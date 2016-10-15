def primefactor(a):
	b=[]
	if a%2==0:
		b.append(2)
		while a%2==0:
			a=int(a/2)
	c=int(a**(1/2))
	for i in range(3,c+1,2):
		if a%i==0:
			while a%i==0:
				a=int(a/i)
			b.append(i)
	if a>2:
		b.append(a)
	return b