# Write a recursive python function to calculate the factorial of a number.

def fact(num):
    if num==0:return 1
    return fact(num-1)*num

print(fact(3))