'''
Write a recursive python function to print first N even natural numbers in reverse
order
'''

def rev_even(num):
    if num>0:
        print(2*num)
        rev_even(num-1)

rev_even(8)