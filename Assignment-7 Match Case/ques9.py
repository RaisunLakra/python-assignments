"""
Write a python script to check whether a given year is
a. Non century leap year
b. Century leap year
c. Non century non leap year
d. Century non leap year
"""
year=int(input("Enter a year : "))

match year:
    case n if year%4==0 and year%100!=0:
        print("Non Century Leap Year")
    case n if year%4==0 and year%100==0 and year%400==0:
        print("Century leap year")
    case n if year%100!=0 and year%4!=0:
        print("Non century non leap year")
    case n if year%100==0 and year%4!=0:
        print("Century non leap year")
    case _:
        print("Non Leap year")