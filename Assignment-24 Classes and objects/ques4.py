# Write a python program to init default values for user object using __init__ method.
class user:
    def __init__(self,name="Johnson Babie Powder",age=28,email=None) -> None:
        self.name=name
        self.age=age
        if email==None:
            self.email=f"{name.lower().split(' ')[0]}@email.com"
        else:
            self.email=email
    
    def __repr__(self) -> str:
        return f"User({self.name}, {self.age}, {self.email})"
    
user1=user()
user2=user("Raisun")
user3=user("Raisun Lakra",25)
user4=user("Raisun Satish Lakra",65,"raisunlakra@gmail.com")

print(user1)
print(user2)
print(user3)
print(user4)