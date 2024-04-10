
#Global scope------------------------------------------------------

a=10 #-> global scope
def fun():
    print(a) #-> access the global scope
fun()


#local scope----------------------------------------------------------

a=10 #-> global scope
def fun():
    a=5 #-> local scope
    print(a) #-> access only local scope in fun()
fun()



#Global & local scope----------------------------------------------------

a=100 #->global scope
def fun():
    a=10 #-> local scope
    print(a)#-> only access the local scope
def fun1():
    print(a) #-> directly access the global scope

fun()
fun1()