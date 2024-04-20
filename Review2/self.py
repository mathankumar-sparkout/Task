#-> self keyword is global of member fun


class self:
    def fun(self,name,age):
        self.name=name
        self.age=age
        print("name is",name)
        print("age is",age)
    def fun1(self):
        print(self.name)
        print(self.age)
class d(self): #-> useing outside of class also
    def fun2(self):
        print(self.name)
        print(self.age)

obj=d()
obj.fun("mathan",24)
obj.fun1()
obj.fun2()

