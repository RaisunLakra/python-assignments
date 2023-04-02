# Write a recursive python function to calculate sum of first N natural numbers

def n_sum(num):
    if num==1:return 1
    return n_sum(num-1)+num

print(n_sum(5))