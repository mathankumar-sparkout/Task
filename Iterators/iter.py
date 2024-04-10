
#iterators

class number():
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a +=1 #->increment value 1
        return x
obj=number()
it=iter(obj)
print(next(it))  #-> first value print  
print(next(it))  #-> second value print







a=(1,2,3,4,5)
obj=iter(a)
print(next(obj)) #-->only 1 value first print 1
               #--> then second value print  2
               #--> last value excute after i

        