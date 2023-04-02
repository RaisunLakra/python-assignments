# Write a recursive python function to calculate sum of first N even natural numbers
def even_sum(num):
    if num==1:return 2*num
    return even_sum(num-1)+2*num

print(even_sum(7))