"""
Write a program to display day name on the basis of user's liking of a colour. Ask
user for his favorite colour. User can answer in a sentence like “I like red colour”.
Assuming all colour name entered by user is in lowercase. Use match case to display
day name associated with the colour.
a. Yellow - Monday
b. Blue - Tuesday
c. Orange - Wednesday
d. White - Thursday
e. Black - Friday
f. Red - Saturday
g. All other colours - Sunday
"""

str=input("What is your favorite color : ").lower()
match str:
    case n if "yellow" in str:
        print("Monday")
    case n if "blue" in str:
        print("Tuesday")
    case n if "orange" in str:
        print("Wednesday")
    case n if "white" in str:
        print("Thursday")
    case n if "black" in str:
        print("Friday")
    case n if "Saturday" in str:
        print("Saturday")
    case _:
        print("Sunday")