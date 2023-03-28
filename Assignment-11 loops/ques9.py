"""
Write a python script to print binary equivalent of a given decimal number. (do not
use bin() method)
"""

num = float(input("Enter a decimal number: "))
integer_part, fractional_part = divmod(num, 1)
print(integer_part)
print(fractional_part)
binary_integer = ''
binary_fractional = ''

integer_part=int(integer_part)

while integer_part > 0:
    quotient, remainder = divmod(integer_part, 2)
    binary_integer = str(remainder) + binary_integer
    integer_part = quotient
print(binary_integer)

if fractional_part != 0:
    binary_fractional = '.'
    for i in range(10):  # set the precision to 10 decimal places
        # fractional_part *= 2
        integer_part, fractional_part = divmod(fractional_part*2, 1)
        binary_fractional += str(int(integer_part))

binary = binary_integer + binary_fractional

print(f"The binary equivalent of {num} is: {binary}")