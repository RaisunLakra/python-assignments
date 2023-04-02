# Write a python program to create a function to find the Min of three numbers

def minimum(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=a and b<=c:
        return b
    else: return c

print(minimum(3,5,2))