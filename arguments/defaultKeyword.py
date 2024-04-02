#positional aguments
def add(name,subject):
    print(f"hii{name}")
    print(f"your subject is{subject}")
add("mathan","english")#--->posional aguments


#keyword aguments
def fun(a,b):
    print(f"a value is{a}")
    print(f"b value is{b}")
fun(10,b=20)#--->b is a keyword aguments  #only keyword aguments follow positional aguments(10 positional,20 keyword)




def fun(a):
    if(a%2==0):
        print("even num")
    else:
        print("odd num")
fun(a=10)  #---> a=10 , a is a keyword



# default aguments

def fun(a=10,b=20):#--->default value is 10,20 fixed a,b
    c=a+b
    print(c)
fun()


def fun(name,age,subject="python"):#--->default use subject name
    print(f"name is{name}")
    print(f"your age is{age}")
    print(f"your subject is{subject}")
fun("mathan",24)#--> positional aguments 

