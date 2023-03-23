# Write a python script to get the last digit from a given number. (for example, if user
# enters 2089 then your output should be 9)
x=int(input("Enter a no. : "))
x%=10
print(x)
x=input("Enter another no. :")
print(int(x[-1]))