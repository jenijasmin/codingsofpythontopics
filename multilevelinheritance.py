#multilevel inheritance.py

class grandfather():
    def ownhouse(self):
        print("this is grandpa house")
class father(grandfather):
    def owncar(self):
        print("this is my fathers car")
class me(father):
    def ownbike(self):
        print("this is my own bike")
o=me()
o.ownhouse()
o.owncar()
o.ownbike()
