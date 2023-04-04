'''
Write a python program to create a School class and 3 instance variables and 1 class
variable
'''

class School : 
    def __init__(self,school_name,board,total_student) -> None:
        self.school_name=school_name
        self.board=board
        self.total_student=total_student
        School.state="Jharkhand"
    
    def __repr__(self) -> str:
        return f'{self.school_name}, {self.board}, {self.total_student}, {School.state}'
    
ram_tahal_choudhary=School("Ram Tahal Choudhary High School","CBSE","3000")

print(ram_tahal_choudhary)