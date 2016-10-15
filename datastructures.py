class Stack():
	__l=["IMPLEMENTATION USING A LIST"]
	def __init__(self):
		Stack.__l=[]
	def push(self,a):
		Stack.__l.append(a)
	def pop(self):
		Stack.__l=Stack.__l[:len(Stack.__l)-1]
	def peek(self):
		return Stack.__l[-1]
class Queue():
	__l=["IMPLEMENTATION USING A LIST"]
	def __init__(self):
		Queue.__l=[]
	def enque(self,a):
		Queue.__l.append(a)
	def dequeue(self):
		Queue.__l=Queue.__l[1:]
	def show(self):
		return Queue.__l[0]
class Circularqueue():
	__l=["IMPLEMENTATION USING A LIST"]
	size=0
	def __init__(self,size):
		Circularqueue.__l=[]
		Circularqueue.size=size
	def enque(self,a):
		while Circularqueue.size >= len(Circularqueue.__l):
			Circularqueue.__l.append(a)
	def dequeue(self):
		Circularqueue.__l=Circularqueue.__l[1:]
	def show(self):
		return Circularqueue.__l[0]