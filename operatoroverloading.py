a=10
b=20
print(a+b)
a="jackshin"
b="riina"
print(a+b)
#it happens bcoz each datatypes are under classes so if we add integers it gets total and if we add string it gets joined.
"""
class addition:
    def __init__(self,a):
        self.a=a

o1=addition(10)
o2=addition(20)
print(o1+o2)#this will not give answer after execution and will show error bcoz we cannot add two objects directly 
"""

class operators:
    def __init__(self,a):
        self.a=a
    def __add__(o1,o2):
        return o1.a+o2.a
o1=operators(10)
o2=operators(30)
print(o1+o2)#this will show answer bcoz we use __add__ property in the function name and caalls the object in that function

class complex:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self,others):
        return self.a+others.a,self.b+others.b
o1=complex(1,1)
o2=complex(3,5)
o3=o1+o2
print(o3)


class comparison:
    def __init__(self,a):
        self.a=a
    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False
ob1=comparison(3)
ob2=comparison(2)
if(ob1>ob2):
    print("correct")
else:
    print("incooreect")
