#abstract base class method in python
from abc import ABC,abstractmethod
class idbi:
    @abstractmethod
    def debit(self):
        pass
    @abstractmethod
    def credit(self):
        pass
    @abstractmethod
    def loan(self):
        pass
class sbi(idbi):
    def debit(self):
        print("monthly of 150rs per year will be debited")
    def credit(self):
        print("your amount will be credited instantly without any network troubles")
    def loan(self):
        print("you can easily get your loan og interest just 7%")
    def app(self):
        print("you can easily access your app in mobile")
o=sbi()
o.debit()
o.credit()
o.loan()
o.app()
