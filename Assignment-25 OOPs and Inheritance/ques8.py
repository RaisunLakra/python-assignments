'''
Write a python script to create a SmartPhone class by inheriting Calculator 2.0 and
Phone Class.
'''
from ques6 import Calculator2
from ques7 import Phone

class SmartPhone(Calculator2, Phone):
    pass
if __name__=="__main__":
    samsung = SmartPhone(4,5)
    m = samsung.mul()
    print(m)
    samsung.calling()