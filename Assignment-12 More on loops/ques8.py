# Write a python script to print first N terms of a Fibonacci series

n=int(input("Enter a no. : "))

a=0
b=1

for i in range(1,n+1):
    print(a)
    c=a+b
    a=b
    b=c