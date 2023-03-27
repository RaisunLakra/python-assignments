# Write a python script to calculate sum of first N even natural numbers
n=int(input("Enter a no. : "))
sum=0
for i in range(1,n+1):
    sum+=2*i
print(sum)