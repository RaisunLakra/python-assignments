# Write a python script to update 2nd Question, add a class variable (platform) and
# create a classmethod to access it.

from ques2 import Update_profile

class Update(Update_profile):
    
    @classmethod
    def update(cls, platform):
        cls.platform=platform

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {Update.platform}"

if __name__=="__main__":
    person2=Update("Raisun Lakra","raisun@gmail.com",26,4473733737,"ranchi")
    Update.update("ranchi station")
    print(person2)