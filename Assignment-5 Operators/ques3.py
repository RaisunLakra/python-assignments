# Write a python script to swap data of two variables
x=input("Enter 1st no : ")
y=input("Enter 2nd no : ")

print("Initially x =",x,"y =",y)

"""
x=x+y
y=x-y
x=x-y
error - unsuported operand type for -: 'str' and 'str'

"""
x,y=y,x

print("Data swapped ")
print("x =",x,"y =",y)