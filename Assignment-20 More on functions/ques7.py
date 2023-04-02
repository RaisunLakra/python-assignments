# Write a python program to access a function inside a function

def squareOf(num):
    return num**2
def sum_of_square(num1,num2):
    sum=0
    for num in range(num1,num2+1):
        sum+=squareOf(num)
    return sum

print(sum_of_square(4,6))