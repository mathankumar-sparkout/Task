#match statement-------------- only matching case work 

character="b"

match character:
    case 'a':
        print("character is 'a'")
    case 'b':
        print("character is 'b'")
    case 'c':
        print("character is 'c'")
    case _:
        print("undefined value")


#-> only match case work otherwise undefined value
def fun():
    a=int(input())
    b=int(input())
    c=input("add/min/div/mul")
    match c:
        case "add":
            print(a+b)
        case "min":
            print(a-b)
        case "div":
            print(a/b)
        case "mul":
            print(a*b)
        case _:
            print("undefined value")
fun()