#global scope

a=10 #-> global value
def fun():
    print(a)
fun()


# local value

def fun():
    a=100  #-> local value
    print(a)
fun()


 #--> global value
class cls:
   global a
   a=100
   def fun(self):
        x=300 #--> local value
        print(x) #-> print local value
   def fun1(self):
       print(a) #-> global value
obj=cls()
obj.fun()
obj.fun1()
