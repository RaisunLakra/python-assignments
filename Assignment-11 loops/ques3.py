# Write a python script to calculate sum of cubes of first N natural numbers
num=int(input("Enter a no. : "))
sum=0
for i in range(1,num+1):
    sum+=(i**3)
print(sum)