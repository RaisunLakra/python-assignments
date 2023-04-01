# Write a python program to multiply all the numbers in a list

def mul_list(lists):
    mul=1
    for e in lists:
        mul*=e
    return mul
print(mul_list([3,4,5,6,7,8]))