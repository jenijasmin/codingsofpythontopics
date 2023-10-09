
"""
#to see all the exceptions
print(dir(locals()['__builtins__']))
print(len(dir(locals()['__builtins__'])))
"""

#most common 5 exceptions
try:
    a=10/0
    print(a)
except Exception as e:
    print("it is a zero division error")





try:
    a=[1,2,3,4,5]
    print(a[10])

except Exception as e:
    print(e)


try:
    a=int("jeni jasmin")
    print(a)
except Exception as e:
    print(e)


try:
    print(x)
except Exception as e:
    print("please write any value to the given varialble")



try:
    fp=open("jeni.txt")
    
except Exception as e:
    print("please enter a valid file")
else:
    print(fp.read())

try:
    a=10/20
    print(a)
    b=[2,4,5]
    print(b[10])
except Exception as e:
    print(e)























