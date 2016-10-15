import datastructures as d
st=d.Stack()
while True:	
	a=list(input("Characthers: "))
	if a != ["z"]:
		for i in range(len(a)):
			st.push(a[i])
	else:
		print("Last Characther was: ",st.peek())
		st.pop()