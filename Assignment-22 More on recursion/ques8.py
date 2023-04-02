# Write a recursive python function to print binary of a given decimal number.

def num_bin(num):
    if num>0:
        num_bin(num//2)
        print(num%2,end="")

num_bin(10)