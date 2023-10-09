
"""#this method is used when we have the read file in same location 
files=open("casting.py","r")
print(files.read())
#or  
try:
    file=open("casting.py","r")
    print(file.read())
except:
    print("file is not found")
    """
#or this method is used when we have read file in different location
f = open('C:\\jensi\readfile', "r")

print(f.read())
