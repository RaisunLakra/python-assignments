# Write a python script to remove the last digit from a given number. (for example, if
# user enters 2534 then your output should be 253)
x=int(input('Enter a no. : '))
print(int(x/10))
x=input("Enter another no. : ")
print(x[:-1]) #type=<char>