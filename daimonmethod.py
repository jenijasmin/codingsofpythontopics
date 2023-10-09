#handling daimond method in python
class a:
    def display(self):
        print("i am A display")
class b(a):
    def display(self):
        print("i am B display")
class c(a):
    def display(self):
        print("i am C display")
class d(b,c):
    def display(self):
        print("i am D display")
o=d()
o.display()
#or
class a:
    def display(self):
        print("i am A display")
class b(a):
    def display(self):
        print("i am B display")
class c(a):
    def display(self):
        print("i am C display")
class d(b,c):
    pass
o=d()
o.display()
