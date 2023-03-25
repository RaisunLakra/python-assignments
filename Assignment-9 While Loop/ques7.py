# Write a python script to print first N even natural numbers in reverse order
n=int(input("Enter value of n : "))
n=n if n%2==0 else n-1
while n>0:
    print(n)
    n=n-2