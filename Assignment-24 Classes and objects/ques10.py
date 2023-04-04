'''
Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables. Also define
instance methods to input fields and display field values
'''

class Employee:
    def __init__(self,empid,name,salary) -> None:
        self.empid=empid
        self.name=name
        self.salary=salary

    def __showData__(self):
        print("Employee Id        :",self.empid)
        print("Employee Name      :",self.name)
        print("Employee Salary    :",self.salary)

emp=Employee(10024,"Raisun Satish Lakra",240000)

emp.__showData__()