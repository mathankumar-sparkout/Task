#try except (value error)
try:
    a=int(input())
    b=int(input())
    print(a+b)
except ValueError as e:
    print("Type int values",e)

try:
    a=int(input())
    b=int(input())
    c=a/b

    print(c)
except ZeroDivisionError as e:
    print("Zero division error",e)

# try multiple except---------------------------------------------------------------------------------
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)

except ValueError as e:            #-->only use int value otherwise value error will excute
    print("correct int value type")
except ZeroDivisionError as e:      #-->10/2=0 zerodivision error will excute
    print("zero diviosion error")
except NameError as e:
    print(" this is name error")     #-->pritt  name error will excute

#try-except-else --------------------------------------------------------------------------
    
    a=int(input())
    b=int(input())
    try:
        c=a/b
    except ZeroDivisionError as e:      #-->10/2=0 zerodivision error will excute
        print("zero diviosion error")
    else:
        print("c value is",c)#--->try block is excute autometically else block work otherwise exception statement work
    
    #raise exception -----------------------------------------------------------------------------------
a=int(input())
b=int(input())
try:
    b==0
    raise Exception #--> b==0 rasie the exception directly go exception
    c=a/b
    print(c)
except:
    print("raise exception") #-->excute


#finally----------------------------------------------------------------------------------------------------
try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except ZeroDivisionError as e:
    print("zero divion error")

finally:
    print("program end") #--->try block exception or correct autometically work on finally 




