# Write a python program to create a function that finds a maximum of four numbers
def maxf(a,b,c,d):
    if a>b and b>c and c>d:
        return a
    elif b>c and c>d:
        return b
    elif c>d:
        return c
    else:
        return d
    
req_num=maxf(1,3,4,2)
print(req_num)