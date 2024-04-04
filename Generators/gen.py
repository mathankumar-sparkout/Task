def myfuncation():#->fun
    a=10
    b=20
    c=a+b
    yield c #-> yield keyword
    yield a
obj=myfuncation()
print(next(obj)) #->iterator value
print(next(obj))



def generators():#--> fun
    a=[1,2,3,4,5] #--> list
    for i in a: #--> i variable in increment a
        yield i # -> yield keyword
var=generators() #-> var variable 
print(next(var)) #-> iterator the value one
print(next(var))
print(next(var))
print(next(var))
print(next(var)) #-> iterator the [1,2,3,4,5] #-> end
print(next(var)) #-> error stop iteraion