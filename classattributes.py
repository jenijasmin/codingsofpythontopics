#class attributes

class student:
    name="jeni"
    age=20
#getattr method
print(getattr(student,'name'))
print(getattr(student,'age'))
print(getattr(student,'gender','female'))
print(student.name)
print(student.age)
#if you want to change or edit attributes we can use setattribute method
setattr(student,'name','basir')
print(student.name)
setattr(student,'id','1001')
print(student.id)
#include new items use this format
student.city="pdkt"
print(student.city)
print(student.__dict__)
delattr(student,'city')
print(student.__dict__)
del student.id
print(student.__dict__)
