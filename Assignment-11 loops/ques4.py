# Write a python script to calculate sum of first N odd natural numbers
num=int(input("Enter a no. : "))
sum=0
for i in range(0,num):
    sum+=2*i+1
print(sum)