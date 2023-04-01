# Write a python program to sum all the numbers in a list.

def list_sum(list):
    sum=0
    for e in list:
        sum+=e
    return sum

print(list_sum([1,2,3,4]))