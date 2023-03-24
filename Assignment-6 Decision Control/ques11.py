# Write a python script to take the month value in numeric format and display the
# number of days in it.
while True:
    x=int(input("Enter month no. : "))
    if x>12 or x<1:
        print("Invalid month no")
        exit()
    else:
        if x==1 or x==3 or x==5 or x==7 or x==8 or x==10 or x==12:
            print("Total no of days = 31")
        elif x==2:
            print("Total no of days = 28 or 29")
        else:
            print("Total no of days = 30")
    print("Enter an invalid month no to exit the loop")