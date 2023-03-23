# Write a python script to calculate the area of Triangle. Number is entered by the user.
import math

print("Enter sides :")
a=int(input('Enter 1st side :'))
b=int(input('Enter 2nd side :'))
c=int(input('Enter 3rd side :'))
s=(a+b+c)/2 #semi perimeter
print("Area of Triangle =",math.sqrt(s*(s-a)*(s-b)*(s-c)))