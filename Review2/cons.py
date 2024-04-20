# construtor------------------------

class con:
    def __init__(self):
        print("hii python")
obj=con()


#parameter construtor--------------------


class con:
    def __init__(self,a,b):#-> argument added
        self.a=a
        self.b=b
    def fun(self): #-> user defined fun usinf self keyword
        print(self.a)
        print(self.b)
        c=self.a+self.b
        print(c)
obj=con(10,20)  #->  add value in arguments --> autometically called fun
obj.fun()