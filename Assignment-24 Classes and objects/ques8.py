'''
WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
order based on the ram size.
'''

class Laptop:
    def __init__(self,brand,ram,cpu,hdd) -> None:
        self.brand=brand
        self.ram=ram
        self.cpu=cpu
        self.hdd=hdd

    def __repr__(self) -> str:
        return f"{self.brand}, {self.ram}, {self.cpu}, {self.hdd}"

    @staticmethod
    def sort(laptops):
        return sorted(laptops,key=lambda laptop:laptop.ram)

laptop1=Laptop("HP",16,"itel i5",256)
laptop2=Laptop("Lenovo",8,"intel i5",256)
laptop3=Laptop("Del",12,"intel i7",500)

laptops=Laptop.sort([laptop1,laptop2,laptop3])
for laptop in laptops:
    print(laptop)