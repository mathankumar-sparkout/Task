#identify operators ---------------------only check memory location

a=10
b=20
print(a is b)
print(id(a))
print(id(b))
#o/p--------> false
#because a memory location is -->140709825497816
# b memory location is-->140709825498136
# so false

def fun():
    a=100
    b=100
    print(a is b)
    print(id(a)) #-> same location of a
    print(id(b))#-> same location of b
fun()
#-> o/p -> true