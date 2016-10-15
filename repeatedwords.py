def repeatedwords(a):
	l,b,j=[],[],0
	a+=" "
	for i in range(len(a)):
		c=a[i]
		if c==" " or c==".":
			l.append(a[j:i])
			j=i+1
	l.append("///")
	count=1
	while l[i]!="///":
		while l[j]!="///":
			if l[i]==l[j] and i!=j :
				l.pop(j)
				j=j-1
				count+=1
			j+=1
		j=0
		i+=1
		b.append(count)
		count=0
a=input()
repeatedwords(a)