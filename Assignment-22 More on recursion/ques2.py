# Write a recursive python function to calculate sum of first N odd natural numbers

def odd_sum(num):
    if num==1:return 1
    return odd_sum(num-1)+num*2-1

print(odd_sum(7))