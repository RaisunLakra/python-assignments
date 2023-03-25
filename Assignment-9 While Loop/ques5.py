# Write a python script to print first N odd natural numbers in reverse order
n=int(input("Enter value of n : "))
n=n-1 if n%2==0 else n
while n>0:
    print(n)
    n=n-2