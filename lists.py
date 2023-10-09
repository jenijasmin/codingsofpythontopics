a=[1,2,3,4,5,6,7,8,9,10]
#to find type
print(a)
print(type(a))
#to find no of values in the list
print(len(a))
#array
print(a[0])
#array slicing
print(a[2:6])
print(a[2:])
print(a[ :8])
#to make copy
b=a.copy()
print(b)
#to find count
print(a.count(8))
#to find index
print(a.index(8))
#to find max
print(max(a))
#to find min
print(min(a))
#allow all types of data types
c=[1,"jeni",True,5.87,["apple",3,"orange"]]
print(type(c))
print("type;:",type(c[0]))
print("type;:",type(c[1]))
print("type;:",type(c[2]))
print("type;:",type(c[3]))
print("type;:",type(c[4][1]))
#pop method
a.pop(1)#removes the values using index
print(a)
a.remove(3)#removes the values using values itself
print(a)
a.append(11)#can add a single items seperately
print(a)
d=["jeni","jack","vasi"]
a.extend(d)#can add a seperate list to previous list
print(a)
#insert
d.insert(1,"papu")
print(d)
#list constructor
e=list("jeni")
print(e)
f=list(range(10))
print(f)
g=[74,75,39,44,9]
print(g)
g.sort()
print(g)
g.sort(reverse=True)
print(g)
h=["dgeh","dheudfh","udhej","ideuidheu"]
h.sort(key=len)
print(h)
