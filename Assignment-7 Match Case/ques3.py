"""
Write a menu driven program with the following options:
a. Check whether a given set of three numbers are lengths of an isosceles
triangle or not
b. Check whether a given set of three numbers are lengths of sides of a right
angled triangle or not
c. Check whether a given set of three numbers are equilateral triangle or not
d. Exit.
"""

from termcolor import colored

while True:
    print(colored("Choose an option:", "magenta"))
    print(colored("a. Check if three numbers form an isosceles triangle", "blue"))
    print(colored("b. Check if three numbers form a right-angled triangle", "blue"))
    print(colored("c. Check if three numbers form an equilateral triangle", "blue"))
    print(colored("d. Exit", "cyan"))

    option = input().lower()

    match option:
        case "a":
            try:
                a = int(input("Enter side 1: "))
                b = int(input("Enter side 2: "))
                c = int(input("Enter side 3: "))
                if a == b != c or a != b == c or a != c == b:
                    print("Isosceles triangle.")
                else:
                    print("The sides do not form an isosceles triangle.")
            except ValueError:
                print(colored("Invalid input. Please try again.", "red", attrs=["underline"]))
        case "b":
            try:
                a = int(input("Enter side 1: "))
                b = int(input("Enter side 2: "))
                c = int(input("Enter side 3: "))
                if a ** 2 + b ** 2 == c ** 2 or a ** 2 == b ** 2 + c ** 2 or a ** 2 + c ** 2 == b ** 2:
                    print("Right-angled triangle.")
                else:
                    print("The sides do not form a right-angled triangle.")
            except ValueError:
                print(colored("Invalid input. Please try again.", "red", attrs=["underline"]))
        case "c":
            try:
                a = int(input("Enter side 1: "))
                b = int(input("Enter side 2: "))
                c = int(input("Enter side 3: "))
                if a == b == c:
                    print("Equilateral triangle.")
                else:
                    print("The sides do not form an equilateral triangle.")
            except ValueError:
                print(colored("Invalid input. Please try again.", "red", attrs=["underline"]))
        case "d":
            exit()
        case _:
            print(colored("Invalid option. Please try again.", "red", attrs=["underline"]))