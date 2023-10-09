class user:
    course="java"
o=user()
print(user.course)
print(user.__dict__)
print(o.__dict__)
o.course="python"
print(o.course)
print(o.__dict__)
print(user.course)
o2=user()
print(o2.course)
