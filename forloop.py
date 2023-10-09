"""
for i in range(5):
    print(i)
for i in range(0,21,2):
    print(i)
for i in range(5):
    a=int(input("enter the number:"))
    b=int(input("enter the number:"))
    print(a+b)
"""

for i in range(0,6,1):
    for j in range(i):
        print(j,end=" ")
    print("  ")
print("---------------------------------------")

for i in range(5,0,-1):
    for j in range(i):
        print(j,end=" ")
    print(" ")
print("---------------------------------------")


for i in range(65,70,1):
    for j in range(65,70,1):
        print(chr(j),end=" ")
    print("  ")
print("---------------------------------------")


for i in range(97,102,1):
    for j in range(97,102,1):
        print(chr(j),end=" ")
    print("  ")
print("---------------------------------------")

