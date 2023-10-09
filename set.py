
#sets in python
a={"jeni","jack","vasi","aadhil","anika","nasreen"}
print(a)
print(type(a))
print("******************************************************")
#for loop in python
for i in a:
     print(i)
print("******************************************************")
#add new elements
a.add("hadiya")
print(a)
print("******************************************************")
#add another set of datas to the previous dats
b={"nabi","nizam","paapu"}
print(b)
#update
b.update(a)
print(b)
#remove
print(a)
a.remove("nasreen")
print(a)
#discad

a.discard("nasreen")
print(a)

#pop
print("********************************")
a.pop()
print(a)
print("********************************")
#to delete it fully
a.clear()
print(a)
print("******************************************************")
#union set
c={1,2,3,4,5}
d={5,6,7,8,9}
e=c.union(d)
print("union set:",e)
#intersection set
e=c.intersection(d)
print("intersection set:",e)
#symmetic difference
e=c.symmetric_difference(d)
print(e)
#joint and disjoint set
print("********************************")
e=c.isdisjoint(d)
print(e)
print("********************************")
x={1,2,3,4,5,6,7,8,9}
y={1,2,3,4}
z=y.issubset(x)
print(z)
#super set(all values in two variables should be equal)
s={7,8,9,10}
t={7,8,9,10}
p=s.issuperset(t)
print(p)

























