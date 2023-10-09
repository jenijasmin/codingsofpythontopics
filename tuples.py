#tuples in python
a=(1,"jeni",2.5,True)
print(a)
print(type(a))
print(type(a[0]))
print(type(a[1]))
print(type(a[2]))
print(type(a[3]))
print(len(a))
print(a[0:])
print(a[1:3])
print(a[-1:])
print(a[-3:-1])

#tuple is immutable ie we cannot change or add items like in list.though we need to add we should convert it into list and then change
b=list(a)
print(b)
b.append("jack")
print(b)
a=tuple(b)
print(a)
print("**********************")
#using for loop in tuple
for i in a:
    print(i)

print("**********************************")
if "jack" in a:
    print("jack is found")
else:
    print("not found")
print("-----------------------------------------------------------------------------------------------------------------------------------")
c=(2)
print(type(c))
c=(2,)
print(type(c))
#nested tuples
tuple1=(1,2,3,4)
tuple2=(5,6,7,8)
tuple3=(tuple1,tuple2)
print(tuple3)
print(tuple3[0])
print(tuple3[1])
print(tuple3[0][2])
print(tuple3[1][3])

x=("jeni",)*3
print(x)

