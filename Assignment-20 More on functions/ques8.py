'''
Write a python program to create a function that accepts a string and calculate the
number of upper case letters and lower case letters.
'''

def countUpperAndLower(string):
    upper=0
    lower=0
    for e in string:
        if e>='A' and e<='Z':
            upper+=1
        elif e>='a' and e<='z':
            lower+=1
    return upper,lower

print(countUpperAndLower("ttHddKJd"))