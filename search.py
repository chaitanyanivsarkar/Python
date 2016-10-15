def binarysearch(l,a):
	front,end=0,len(l)-1
	while front<=end:
		mid=(front+end)//2
		if a==l[mid]:
			return mid
		elif a>l[mid]:
			front=mid+1
		elif a<l[mid]:
			end=mid
def search(l,a):
	for i in range(len(l)):
		if l[i]==a:
			return i