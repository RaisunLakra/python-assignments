# Write a recursive python function to print octal of a given decimal number

def dec_to_oct(num):
    if num>7:
        dec_to_oct(num//8)
    print(num%8,end='')

dec_to_oct(56)