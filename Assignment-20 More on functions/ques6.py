'''
Write a python program to create a function and print a list where the values are
square of numbers between 1 and 30
'''
def get_square_list():
    li=[]
    for i in range(1,31):
        li.append(i**2)
    print(li)

get_square_list()