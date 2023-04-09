# Write a python script to create a Profile class with 3 attributes (name, email, age).

class Profile:
    def __init__(self,name,email,age) -> None:
        self.name=name
        self.email=email
        self.age=age
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.email}, {self.age}"
    
# creating of person1 object ouside the main function can cause to creating it in the file which imports it
# so to avoid importing of person1 object to child class we make the person1 object inside main method
# person1=Profile("Raisun Lakra","raisun@gmail.com",25)
# print(person1)

if __name__=="__main__":
    person1=Profile("Raisun Lakra","raisun@gmail.com",25)
    print(person1)