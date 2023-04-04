'''
Write a python program to create a Laptop class with 4 attributes (brand, ram, cpu,
hdd) and 2 methods (showConfig() to print the values, __init__() to initialize the
values).
'''

class Laptop:
    def __init__(self, brand, ram, cpu, hdd) -> None:
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd
    
    def showConfig(self):
        print('Brand :',self.brand)
        print("RAM   :",self.ram)
        print("CPU   :",self.cpu)
        print("HDD   :",self.hdd)

hp = Laptop("HP","16 GB","itel i5","265 GB")
hp.showConfig()