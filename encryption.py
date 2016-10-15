import string
def search(l,a):
	for i in range(len(l)):
		if l[i]==a:
			return i
class Encryption():
	__key1=0
	__key2=0
	def __init__(self,key1,key2):
		Encryption.__key1=key1
		Encryption.__key2=key2
	def fileinit(self,a):
		self.f=open(a,"r")
		self.content=self.f.read()
		self.f.close()
		self.f=open(a,"w")
	def hashing(self):
		self.g=""
		self.l=list("qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./1234567890-=`~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?")
		self.l.sort()
		for i in range(len(self.content)):
			self.j=((search(self.l,self.content[i]))**Encryption.__key1)%Encryption.__key2
			self.g+=str(self.j)
	def writing(self):
		self.f.write(self.g)
		self.f.close()
encrypt=Encryption(3,10)
f=input("Enter the file to be encrypted: ")
encrypt.fileinit(f)
encrypt.hashing()
encrypt.writing()