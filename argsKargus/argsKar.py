#*args

def fun(*agrs):  #->using only one argument 
    for i in agrs:
        print(i)
fun(10,20,30,40)#->but multiple values


#**kwargs    keyword arguments

def fun(**kwargs):
    for i,j in kwargs.items():
        print(i,j)
fun(a=10,b=20,c=30) # set value in keywords a,b,c