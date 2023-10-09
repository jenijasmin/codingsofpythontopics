"""
def firstfunction():
    print("tutor joes")
    print("jeni jasmin")
firstfunction()
firstfunction()
firstfunction()
firstfunction()
firstfunction()


print("---------------------------------------------------")
#no return type without argument function in python
def add():
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    c=a+b
    print(c)

add()
print("---------------------------------------------------")
#no return type with argument function in python
def sub(a,b):
    c=(a-b)
    print(c)
sub(25,2)
print("---------------------------------------------------")
"""


"""
#return type without arguments in python
def mul():
    a=int(input("enter a no:"))
    b=int(input("enter a no:"))
    c=a*b
    return c
x=mul()
print("multiplication:",x)

"""
"""
#return type with arguments in python
def div(a,b):
    c=(a/b)
    return c
x=div(100,10)
print(x)
print("---------------------------------------------------")
"""
"""
#arbitary argument function in python
def class1(*students):
    print(students)
    for i in students:
        print(i)
class1("ram","sam","raja","praba")
print("---------------------------------------------------")
"""
"""
#arguments keywords in python
def user(name,age):
    print(name,age)
user(name="jeni",age=20)
"""
#arbitary keywords argument in python(**)
def biodata(**details):
    print(details)
biodata(name="jeni",age=25,gender="female")


#default parameter in python
def details(name,city="pdkt"):
    print(name,"is from",city)
details("jeni",)
details("mercy","kbkd")

details("sri","madurai")

details("vaish",)

details("nisha","perungalur")

#passing as a list argument in python
def total(marks):
    return max(marks)
print(total([78,79,80,81,82]))


#recursive function
def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
print(factorial(5))

#LAMBDA FUNCTION
x=lambda a,b:a*b
print(x(20,10))


















































