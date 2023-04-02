'''
Write a python program to create a function that takes a number as a parameter and
checks if the number is prime or not
'''

def isprime(num):
    if num<2: return False
    for e in range(2,int(num**0.5+1)):
        if num%e==0:
            return False
    return True

print(isprime(7))
print(isprime(8))