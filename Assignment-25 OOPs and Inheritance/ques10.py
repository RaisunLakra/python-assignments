'''
Write a python script to add the new method in SmartPhone class which accepts
Truecaller object as a parameter and call the fetch method of Truecaller.
'''

from ques9 import TrueCaller
from ques6 import Calculator2
from ques7 import Phone

class SmartPhone(Calculator2, Phone, TrueCaller):
    pass
if __name__=="__main__":
    samsung = SmartPhone(4,5)
    m = samsung.mul()
    print(m)
    samsung.calling()
    samsung.add_entry("Raisun Lakra",70)
    samsung.fetch_name(70)


    # wrong answer