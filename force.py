f=open("a.txt","w")
G=6.67*10**(-19)
K=9*10**9
class Particle():
	def __init__(self,m,q,vx,vy,x,y):
		self.m=m
		self.q=q
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
		self.v=(self.vx**2)+(self.vy**2)
	def Mass(self):
		self.m=self.m/((1-((self.v**2)/(9*10**16)))**(1/2))
class Force(Particle):
	def __init__(self,m,q,vx,vy,x,y,M,Q,Vx,Vy,X,Y):
		Particle.__init__(self,m,q,vx,vy,x,y)
		self.M=M
		self.Q=Q
		self.X=X
		self.Y=Y
		self.Vx=Vx
		self.Vy=Vy
	def getacc(self):
		self.a1x=-((G*self.M/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.x-self.X))-((K*self.Q*self.q/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.x-self.X)/self.M)
		self.a1y=-((G*self.M/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.y-self.Y))-((K*self.Q*self.q/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.y-self.Y)/self.M)
		self.a2x=((G*self.M/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.x-self.X))+((K*self.Q*self.q/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.x-self.X)/self.M)
		self.a2y=((G*self.M/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.y-self.Y))+((K*self.Q*self.q/(((self.x-self.X)**2)+((self.y-self.Y)**2))**(3/4))*(self.y-self.Y)/self.M)
	def getvel(self):
		self.vx+=self.a1x*0.01
		self.vy+=self.a1y*0.01
		self.Vx+=self.a2x*0.01
		self.Vy+=self.a2y*0.01
	def getpos(self):
		self.x+=self.vx*0.005
		self.y+=self.vy*0.005
		self.X+=self.Vx*0.005
		self.Y+=self.Vy*0.005
		f.write(str(self.x)+","+str(self.y)+"\n")
p=Particle(1,10**-9,12,12,100,0)
q=Force(1,10**-9,0,12,100,0,100,10**-7,0,0,0,0)
while True:
	p.Mass()
	q.getacc()
	q.getvel()
	q.getpos()
	f.flush()