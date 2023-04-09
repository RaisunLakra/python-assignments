'''
Write a python script to create a Calculator 2.0 class with 2 methods for multiplication
and division of 2 values and inherit it from the Calculator class.
'''

from ques5 import Calculator

class Calculator2(Calculator):
    def mul(self):
        return self.a*self.b
    
    def div(self):
        try:
            return self.a//self.b
        except ZeroDivisionError:
            print("denominator must not be zero.")
        except Exception as e:
            print(e)

if __name__=="__main__":
    cal=Calculator2(3,4)
    print(cal.add())
    print(cal.sub())
    print(cal.mul())
    print(cal.div())
