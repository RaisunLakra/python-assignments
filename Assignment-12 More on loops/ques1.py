# Write a python script to reverse a number
num=int(input("Enter a no. : "))

reverse=''
for digit in str(num):
    reverse=digit+reverse
print(int(reverse))