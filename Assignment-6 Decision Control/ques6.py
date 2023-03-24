# Write a python script to check whether a given number is a three digit number or not.
x=int(input("Enter a no. : "))
if x<=999 and x>=100:
    print("Three digit no.")
else:
    print("not a three digit no.")