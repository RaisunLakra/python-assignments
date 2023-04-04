# Write a python program to create a user class with a method to greet the user.

class user:
    def greet(self,name):
        print("Happy Birthday",name)

user1=user()
user1.greet(input("Enter name : "))