# Write a python program to delete the age property of the user.
class user:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
    
    def __repr__(self) -> str:
        try:
            return f"{self.name},{self.age}"
        except AttributeError:
            print("Age attribute not found")
            return "Age is not available."
    
user1=user("Raisun",24)
print(user1)

del user1.age
print("Age is deleted")
print(user1)