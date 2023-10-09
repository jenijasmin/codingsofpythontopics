class employee:
    def work_hrs(self):
        self.hrs=50
    def print_hrs(self):
        print("total working hrs is",self.hrs)
class trainee(employee):
    def work_hrs(self):
        self.hrs=60
o=employee()
o.work_hrs()
o.print_hrs()
o1=trainee()
o1.work_hrs()
o1.print_hrs()
print("______________________________________________________________________________________________")
#suddeny if a trainee has become an employee and the working hrs should be changed we can do like this
class employee:
    def work_hrs(self):
        self.hrs=50
    def print_hrs(self):
        print("total working hrs is",self.hrs)
class trainee(employee):
    def work_hrs(self):
        self.hrs=60
    def reset_hrs(self):
        super().work_hrs()
o=employee()
o.work_hrs()
o.print_hrs()
o1=trainee()
o1.reset_hrs()
o1.print_hrs()



    


    
