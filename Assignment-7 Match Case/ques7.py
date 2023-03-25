# Write a python program to check whether a given number is positive, negative or
# zero using match case statement
try:
    num=int(input("Enter a no : "))
    match num:
        case n if num>0:
            print("Positive")
        case n if num==0:
            print("Zero")
        case _:
            print("Negetive")
except ValueError:
    print("Invalid Input\nPlease enter a no.\nTry again")