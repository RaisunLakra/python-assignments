# Write a python program to create 2 objects of the user class and assign different values.

class user:
    n=1
    id=1001
    def __init__(self,name) -> None:
        self.name=name
        user.n+=1
        user.id+=1
        self.id=user.id
    def __str__(self) -> str:
        return f"{self.id} - {self.name}"

person1=user(input(f"User {user.n} \nEnter name : "))
person2=user(input(f"User {user.n} \nEnter name : "))
print(person1)
print(person2)