# Write a python script to check whether a given year is a leap year or not
year=int(input("Enter year : "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("Leap year")
else:
    print("not a leap year")