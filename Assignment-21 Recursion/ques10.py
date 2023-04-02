# Write a recursive python function to print a number in reverse order

def rev(num):
    if num>0:
        print(num%10,end="")
        rev(num//10)

rev(3456)