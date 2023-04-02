'''
Write a python program to create a function to check whether a string is a pangram
or not
'''

# Panagram is a word or sentence which comtain all english alphabet atleast one.
def is_pangram(string):
    for e in 'abcdefghijklmnopqrstuvwxyz':
        if e not in string.lower():
            return False
    return True

print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("The quick brown fox over the lazy dog"))