# Write a python script which takes a three digit number from the user and displays only its first digit.
x=input("Enter a three digit no. : ")
print(int(x[0])) #wrong output for no. less than 3 digit
print("Another no ")
x=int(input())
print(x//100) # wrong output for no. grater than 3 digit