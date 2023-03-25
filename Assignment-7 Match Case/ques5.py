"""
Write a program which takes a number from user. Print Saurabh Shukla if the number
is even, print Prateek Jain if the number is negative odd number and print Aditya
Choudhary if number is positive odd number
"""

try:
    num=int(input("Enter a number : "))
    match num:
        case n if num>=0 and num%2==0:
            print("Saurabh Sukla")
        case n if num<0:
            print("Prateek")
        case n if num>0:
            print("Aditya Choudhary")
except ValueError:
    print("Invalid Input. Try again")
except Exception as e:
    print(e)