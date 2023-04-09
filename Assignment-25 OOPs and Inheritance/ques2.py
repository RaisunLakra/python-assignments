# Write a python script to update the above Profile class with encapsulation
from ques1 import Profile

class Update_profile(Profile):
    def __init__(self, name, email, age, phone_no, city) -> None:
        super().__init__(name, email, age)
        self._phone_no=phone_no
        self._city=city
    
    def get_phone_no(self):
        return self._phone_no
    
    def get_city(self):
        return self._city
    
    def set_phone_no(self,phone_no):
        self._phone_no=phone_no
    
    def set_city(self, city):
        self._city=city

    def __repr__(self) -> str:
        return f"{super().__repr__()},{self._phone_no},{self._city}"

    # def __repr__(self) -> str:
    #     return f"{self.name}, {self.age}, {self.email}, {self._phone_no}, {self._city}"

if __name__=="__main__":
    person2=Update_profile("Raisun Lakra","raisun@gmail.com",26,4473733737,"ranchi")
    print(person2)