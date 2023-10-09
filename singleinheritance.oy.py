class apple:
    brand="iphone"
    types="promax"
    city="chennai"
    instaid="@apple"
    def link(self):
        print("link:iphone.com")
class apple153(apple):
    def __init__(self):
        self.name="iphone 15 pro max"
        self.year=2023
    def printall(self):
        print("name:",self.name)
        print("year:",self.year)
        print("brand:",self.brand)
        print("types:",self.types)
        print("city:",self.city)
        print("instaid:",self.instaid)
o=apple153()
o.printall()
o.link()
        
