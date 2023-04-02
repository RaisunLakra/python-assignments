# Write a recursive python function to print first N natural numbers

def natural_no(num):
    if num>0:
        natural_no(num-1)
        print(num)

natural_no(9)