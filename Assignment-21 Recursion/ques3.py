# Write a recursive python function to print first N odd natural numbers

def odd(num):
    if(num>0):
        odd(num-1)
        print(2*num-1)

odd(7)