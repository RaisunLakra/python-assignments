# Write a python script to print first M multiples of N.
print("Print m multiple of n")
n=int(input("Enter value of n : "))
m=int(input("Enter value of m : "))

for i in range(1,m+1,1):
    print(n*i)