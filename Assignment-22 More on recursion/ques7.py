# Write a recursive python function to calculate sum of the digits of a given number
def sum(num):
    if num==0:return 0
    return sum(num//10)+num%10
    
print(sum(458))