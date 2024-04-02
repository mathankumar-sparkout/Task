character = 'A'

match character:
    case 'A':                 # find the a character in matching statment 
        print("character is A")
    case 'B':
        print("character is B")
    case 'C':
        print("character is C")
    


a=int(input())
b=int(input())
c=input("/add/mul/div/min :")   # user input matching case

match c:
    case 'add':
        print(a+b)
    case 'mul':
        print(a*b)
    case 'div':
        print(a/b)
    case 'min':
        print(a-b)


        
