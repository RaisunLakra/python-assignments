'''
Write a python program to create a function to check whether a number falls in a
given range.
'''

def c(ran1,ran2,number):
    for e in range(ran1,ran2):
        if e==number:
            return True
    return False

print(c(9,88,45))