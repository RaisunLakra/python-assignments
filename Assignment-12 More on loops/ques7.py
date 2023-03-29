"""
Write a python script to check whether a given pair of numbers are co-Prime
numbers or not.
"""
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

num1=int(input("Enter a no. : "))
num2=int(input("Enter another no. : "))

if gcd(num1,num2)==1:
    print("co-prime")
else:
    print("Not a co-prime")