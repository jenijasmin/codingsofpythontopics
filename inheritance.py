#inheritance in python
class mobile:
    origin="india"
    rate="three million+"
    def vivo(self):
        print("it is one of the branded company")
class redmi(mobile):
    def __init__(self):
        self.name="redmi blue"
        self.model="redmi12"
    def printdetails(self):
        print(self.name)
        print(self.model)
        print(self.origin)
        print(self.rate)
o=redmi()
o.printdetails()
o.vivo()
print("************************************************************************************************************************************************")        
class student:
    name="jeni"
    age=20
    def studies(self):
        print("completed bsc maths with 80%")
class std_details(student):
    def __init__(self):
        self.number=756465776
        self.addr="chennai"
    def printall(self):
         print(self.name)
         print(self.age)
         print(self.number)
         print(self.addr)
o1=std_details()
o1.printall()
o1.studies()
