def fun(name:str)->str:
    print(f"name is{name}")
fun("mathan")
print(fun.__annotations__)# name is a string so identifi user str -->output



def fun(a:int,b:int)->int: #a,b is a int value identifie user
    c=a+b
    print(c)
fun(10,20)
print(fun.__annotations__)