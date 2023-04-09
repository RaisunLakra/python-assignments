'''
Write a python script to update 2nd Question, change email and age to __email and
__age.
'''
from ques2 import Update_profile
class Update_class(Update_profile):
    def __init__(self, name, email, age, phone_no, city) -> None:
        super().__init__(name, phone_no, city)
        self.__email=email
        self.__age=age

    def set_email(self, email):
        self.__email=email

    def get_email(self):
        return self.__email
    
    def set_age(self, age):
        self.__age=age
    
    def get_age(self):
        return self.__age
    
    def __repr__(self) -> str:
        return f"{self.name}, {self.__email},{self.__age}, {self._phone_no}, {self._city}"

if __name__=="__main__":
    person2=Update_profile("Raisun Lakra","raisun@gmail.com",26,4473733737,"ranchi")
    print(person2)
