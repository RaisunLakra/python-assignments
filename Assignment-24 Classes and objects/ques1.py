# Write a python program to create a user class with 3 properties : name, age, email.

class info:
    name=''
    age=9
    email='sample@mnnit.ac.in'
    def __init__(self,name,age,email) -> None:
        self.name=name
        self.age=age
        self.email=email

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.email}"

i1=info('Raisun',26,'raisun.2022ca074@mnnit.ac.in')
print(i1)