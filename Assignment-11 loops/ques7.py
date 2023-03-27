# Write a python script to count digits in a given number
"""
num=int(input("Enter a no. : "))
count=0
while num!=0:
    count=count+1
    # num/=10 # will give error as it provide decimal no
    num//=10
print(count)
"""
num=float(input("Enter a no. : "))
str_num=str(num).strip('0')
count=sum(c.isdigit()for c in str_num)
print(count)

"""
NOTE: when we enter a no. like 456 float convert it into floating point no.
as '456.0'. In next line str convert it into string and strip method removes any leading and
trailing zero from it.
In next line, inside sum method isdigit return true value for digit and sum method return summation
of them
eg. True+True=2
    True+True+True=3
Finally we return count
"""