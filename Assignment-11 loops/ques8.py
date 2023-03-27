# Write a python script to calculate sum of digits of a given number
num=float(input("Enter a no. : "))
str_num=str(num).strip('0')
sum=0
for x in str_num:
    if x.isdigit():
        sum+=int(x)
print(sum)