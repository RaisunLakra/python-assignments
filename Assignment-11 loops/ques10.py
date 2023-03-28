# Write a python script to print the octal equivalent of a given decimal number. (do not
# use oct() method)
num=float(input("Enter a no. : "))
integer_part,fractional_part=divmod(num,1)

oct_int=''
oct_frac=''

while integer_part>0:
    quotient,remainder=divmod(integer_part,8)
    oct_int=str(int(remainder))+oct_int
    integer_part=quotient
print(oct_int)

if fractional_part!=0:
    oct_frac='.'
    for i in range(10):
        quotient,remainder=divmod(fractional_part*8,1)
        oct_frac+=str(int(quotient))
        fractional_part=remainder

octal_equivalent=oct_int+oct_frac

print(f"Binary Octal equivalent of {num} = {octal_equivalent}")
print()