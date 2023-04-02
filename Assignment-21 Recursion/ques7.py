# Write a recursive python function to print squares of first N natural numbers

def square_nos(num):
    if num>0:
        square_nos(num-1)
        print(num**2)

square_nos(8)