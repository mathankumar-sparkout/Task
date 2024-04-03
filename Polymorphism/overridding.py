class animal():
    def cat(self):
        print("cat sound")
class birds(animal):
    def cat(self):#..>same fun name in 2 nd class ,call the 2 nd fun ,2 nd function only called 
        print("bird sound")
obj=birds()
obj.cat()