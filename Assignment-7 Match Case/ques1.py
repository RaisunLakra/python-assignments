# Write a python script to display the number of days in a given month number.
month=int(input("Enter no. of months : "))

if (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
    print("no of days = 31")
elif month==2:
    print("no of days = 29/28")
else:
    print("no of days = 30")