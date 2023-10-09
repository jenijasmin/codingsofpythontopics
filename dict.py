user={
    "name":"jeni",
    "age":20,
    "marietalstatus":"no"
    }
print(user)
print(user["name"])
print(user.get("age"))
print(user.keys())
print(user.values())
print(user.items())

#for loop
for x,y in user.items():
    print(x,":",y)
for x in user.keys():
    print(x)
for x in user.values():
    print(x)
#if else statement
if "age" in user:
    print("yes")
else:
    print("no")
if "gender" in user:
    print("yes")
else:
    print("no")
#changing values
user.update({"gender":"male"})
print(user)
user["gender"]:"female"
print(user)
user.pop("age")
print(user)

#nested dictionary
users={
    "user1": {
        "name":"jeni",
            },
"user2": {
        "name":"jack",
        }
        }
print(users)










users={
    "user1": {
        "name": "Ram",
        "age": 25,
        "isMarried": True
    },
"user2": {
        "name": "SAm",
        "age": 35,
        "isMarried": False
    }
}
print(users)










