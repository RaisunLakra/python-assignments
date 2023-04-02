# Write a recursive python function to print first N natural numbers in reverse order

def rev_natural_no(num):
    if num>0:
        print(num)
        rev_natural_no(num-1)

rev_natural_no(9)