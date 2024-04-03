#private value
class bank():
    def __init__(self):#--->private method
        self.__value=10 #-->private value   
    def person1(self):#-->public method
        print("id=1")
        print("account_num:123")
        print("amount=10000")
        print("address=chennai")
    def person2(self):#-->public method
        print("id=2")
        print("account_num:456")
        print("amount=20000")
        print("address=coimbatore")
obj=bank()
obj.person1()
obj.person2()
print("value:",obj.__value)#-->doen't access the otside of the value 



#private method access the public funcation

class bank():
    def __init__(self):#--->private method
        self.__value=10 #-->private value   
    def person1(self):#-->public method
        print("value:",self.__value)#-->access the private value in member public funcation
        print("id=1")
        print("account_num:123")
        print("amount=10000")
        print("address=chennai")
    def person2(self):#-->public method
        print("id=2")
        print("account_num:456")
        print("amount=20000")
        print("address=coimbatore")
obj=bank()
obj.person1()#-->access the private value
obj.person2()
        


#private method access the public method

class bank():
    def __init__(self):#--->private method
        self.__value=10 #-->private value   
    def __person1(self):#-->private method
        print("value:",self.__value)#-->private value 
        print("id=1")
        print("account_num:123")
        print("amount=10000")
        print("address=chennai")
    def person2(self):#-->public method
        self.__person1()#-->access the private method
        print("id=2")
        print("account_num:456")
        print("amount=20000")
        print("address=coimbatore")
obj=bank()
obj.person2()#-->acess the private method in object












