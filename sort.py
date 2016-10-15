def bubble(l):
	for i in range(len(l)):
		for j in range(len(l)-i-1):
			if l[j]>l[j+1]:
				l[j],l[j+1]=l[j+1],l[j]
	return l
def radixnum(l):
	g=[]
	for i in range(len(l)):
		g.append(l[i])
	m=len(str(max(l)))
	for j in range(1,m+1):
		a=[[],[],[],[],[],[],[],[],[],[]]
		k=0
		f=[]
		for i in range(len(l)):
			b=(l[i]-((l[i]//10**j)*10**j))//(10**(j-1))
			f.append(b)
			a[b].append(l[i])
		for i in range(10):
			for j in range(len(a[i])):
				if a[i][j] in g:	
					l[k]=a[i][j]
					k+=1
	return l
l=eval("["+input()+"]")
b=radixnum(l)
print(b)
c=bubble(l)
print(c)