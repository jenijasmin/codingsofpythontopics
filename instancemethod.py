class topper:
    name="jack"
    age=15
    def rank(self,gender):
        print("name=",topper.name)
        print("age=",topper.age)
        print("gender=",gender)
o=topper()
o.rank("female")
topper.rank(o,"female")


