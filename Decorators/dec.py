def a(func):#-->function a argument func
    def b():
        print("hii")
        func() #-->argument func
        print("hello")
    return b #-> return b funcation
@a
def c():  #--> function
    print("welcome")
c() #-->call the c function


def mydec(fun): #->function fun is a agument
    def a():
        print("welcome to")
        fun()
    return a
@mydec #->dec call
def myfunction():
    print("hello python")
myfunction()
@mydec
def b():
    print("decorators")
b()