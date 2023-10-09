#multiple inheritance in python
class father():
    def work(Self):
        print("he is a business man")
    def hobby(self):
        print("he plays cricket")
class mother():
    def works(self):
        print("she is house wife")
    def hobbys(self):
        print("she reads book")
class son(father,mother):
    def sons_act(self):
        print("he is studying")
o2=son()
o2.sons_act()
o2.work()
o2.hobby()
o2.works()
o2.hobbys()
