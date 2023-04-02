'''
Write a python program to create a function that checks whether a passed string is
palindrome or not.
'''
def palindrome(string):
    i=0;j=len(string)-1
    while i<j:
        if string[i]!=string[j]:
            return False
        i+=1;j-=1
    return True
print(palindrome("tthtt"))
print(palindrome("tgh"))