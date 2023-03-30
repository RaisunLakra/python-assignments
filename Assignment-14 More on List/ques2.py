# Write a Python script to create a list of first N odd natural numbers.

num=int(input("Enter a no. : "))

list=[2*i+1 for i in range(num)]
print(list)