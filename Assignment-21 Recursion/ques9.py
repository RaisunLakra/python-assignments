# Write a recursive python function to print first N multiples of a given number

def mul(num,n):
    if n>0:
        mul(num,n-1)
        print(num*n)

mul(9,10)