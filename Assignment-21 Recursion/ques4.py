# Write a recursive python function to print first N odd natural numbers in reverse order

def rev_odd(num):
    if num>0:
        print(2*num-1)
        rev_odd(num-1)

rev_odd(8)