import datetime
#to find the exact date and time now
x=datetime.datetime.now()
print(x)
print("---------------------------------------------")
#to find onnly today date
y=datetime.date.today()
print(y)
print("---------------------------------------------")

#to create new date
z=datetime.date(2003,1,3)
print(z)
print("---------------------------------------------")
#to see the current time
a=datetime.datetime.now()
print(a)
print("---------------------------------------------")
#to check difference between two dates
c=datetime.datetime.now()
d=datetime.datetime(2024,1,1)
e=d-c
print(e)
print("---------------------------------------------")

#to see the datetime in sting format
x=datetime.datetime.now()
print(x)
y=x.strftime("%A %B %d %Y")
print(y)
print("---------------------------------------------")


