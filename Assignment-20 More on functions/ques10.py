'''
Write a python program to create a function to check whether a string is an anagram
or not.
'''

# Anagram is a word or phrase which formed by rearanging the letters of another word or phrase

def is_anagram(string1,string2):
    for e in string1:
        if e not in string2:
            return False
    for e in string2:
        if e not in string1:
            return False
    return True

print(is_anagram("aba","aab"))
print(is_anagram("aba","a ab"))