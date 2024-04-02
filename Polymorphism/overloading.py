class parent():
    def add(self,a,b):
        c=a+b
        print(c)
    def add(self,a,b,f=0):
        d=a+b+f
        print(d)
    def add(self,a,b,u=0,v=0):
        z=a+b+u+v
        print(z)
obj=parent()
obj.add(10,20)
obj.add(10,20,30)
obj.add(30,19,11,30)