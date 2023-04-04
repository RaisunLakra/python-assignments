# Write a python program to create 3 user objects and find the youngest of all.

class user:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def youngest_one(self,second,third):
        if self.age<=second.age and self.age<=third.age:
            return self.name
        if second.age<=self.age and second.age<=third.age:
            return second.name
        else:
            return third.name
    
rahul=user("Rahul",45)
rishi=user("Rishi Raj",32)
raisun=user("Raisun",27)

print(raisun.youngest_one(rahul,rishi),"is the youngest")