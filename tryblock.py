#try block in python
try:
    a=10/100
except Exception as e:
    print(e)
else:
    print(a,"it is corect")
finally:
    print("thank you")

print("__________________________________")

try:
    a=10/0
except Exception as e:
    print(e)
else:
    print(a,"it is corect")
finally:
    print("thank you")
