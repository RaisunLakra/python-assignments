'''
Write a recursive python function to calculate sum of squares of first N natural
numbers
'''

def sum_sqr(num):
    if num==1:return 1
    return sum_sqr(num-1)+num**2

print(sum_sqr(2))