Private variable and function
class Bank :
    def __init__(self):
        self._bal=500
        self.__bal=500
        self.__deposit
    def withdraw(self):
        a=input("enter the amoutnt to be withdrawn")
        if a<=self.__bal:
            self.__bal-=a
            return self.__bal
        else :
            print "!!get lost!!"
    def __deposit(self):
        a=input("enter the amoutnt to be deposited")
        self.__bal+=a
        return self.__bal
    def show(self):
        print self.__bal
b=Bank()
print b._bal
b.show()
a1=raw_input("enter your choice w\d : ")
if a1=="w":
    c=b.withdraw()
    print c
elif a1=="d":
    c=b.__deposit()
    print c
