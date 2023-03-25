""" 
Write a program which takes user's age and display the category of person. Age
below 10 years- Kid, Age below 20 - Teen, Age below 40 - young, Age below 60 -
Experienced, Age above or equal 60 - Senior Citizen
"""

print("Enter age : ")
try:
    age=int(input())
    if(age<=0):
        print("Inavalid Input")
        exit()
    match age:
        case n if age<=10:
            print("kid")
        case n if age<=20:
            print("Teen")
        case n if age<=40:
            print("young")
        case n if age<=60:
            print("Experienced")
        case n if age<=200:
            print("Senior Citizen")
        case _:
            print("Already dead...")
            print("Sorry")
            print("Bhagwan apki atma ko santi de")
except ValueError:
    print("Invalid Input. Please enter a no. Try again")