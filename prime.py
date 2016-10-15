
def prime_generator(a):
	b=list(range(2,a+1))
	i,j=0,0
	while b[i]!=a:
		while b[j]!=a:
			if (int(b[j]))%(int(b[i])) == 0 and i!=j :
				b.pop(j)
				j=j-1
			j+=1
		j=0
		i+=1
	return b[:-1]