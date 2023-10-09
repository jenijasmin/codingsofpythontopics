#identity operator(main:is,is not)
a=[1,2,3,4]
b=[1,2,3,4]
c=a
print("a is c:",a is c)
print("c is a:",c is a)
print("a is b:",a is b)
print("a is not b:",a is not b)
print(id(a))
print(id(c))
print(id(b))
#to compare the values inside the objects just do with comparison operator
if a==b:
    print("yes")
else:
    print("no")
