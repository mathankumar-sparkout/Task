# Remove--------------------------
a=[1,2,3,4,5]
a.remove(1) #-> remove mentioned value
print(a)


a=[10,20,30,40,50]
b=[1,2,3,4,5]
c=[]
a.remove(10) #a list 10 remove
b.remove(2)  # b list 2 remove
c.append(a)
c.append(b)
print(c)

#pop---------------------------------

a=[1,2,3,4,5]
a.pop()  #-->last element remove
print(a)


a=[10,20,50,70]
b=[5,6,7,8,9]
c=[]

a.pop()
b.pop()
c.append(a) #--> last elemt remove 
c.append(b)
print(c)

# DEl-----------------------------------

a=[1,2,3,4,5]
del a[0] #-> mentioned index value deleted
print(a)


a=[53,23,4,5,6]
b=[2,4,6,7,9]
c=[]
del a[2] #-> index value 2 deleted
del b[1] #-> index value 1 deleted
c.append(a)
c.append(b)
print(c)

# clear---------------------------------

a=[1,2,3,4,5,6,7]
b=[5,6,7,8,9]
a.clear()
b.clear()
print(a)
print(b)
