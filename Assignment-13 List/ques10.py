"""
Write a Python script to create a list, where each element of the list is a digit of a
given number.
"""

mylist=[]
while True:
    number=input("Enter a no.(or 'q' or 'Q' to exit) : ")
    if number.lower()=='q':
        break
    if number.isnumeric()==False:
        print("Invalid Input")
        break
    mylist.append([int(digit) for digit in number])
print(mylist)