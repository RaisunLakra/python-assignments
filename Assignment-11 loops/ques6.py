# Write a python script to calculate factorial of a given number
n=int(input("Enter a no. : "))
mul=1
for i in range(1,n+1):
    mul*=i
print(mul)