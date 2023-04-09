'''
Write a python script to create a Calculator class with 2 methods for adding and
subtracting 2 values.
'''

class Calculator:
    def __init__(self,a=0,b=0) -> None:
        self.a=a
        self.b=b

    def add(self,a=0,b=0):
        return self.a+self.b
    
    def sub(self,a=0,b=0):
        return self.a-self.b

if __name__=="__main__":
    cal = Calculator(4, 5)
    print(cal.add())
    print(cal.sub())