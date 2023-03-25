# Write a menu driven program to perform following operations - Addition, Subtraction, Multiplication, Division
while True:
    print("Enter an operation")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    print()

    try:
        op=int(input())
        match op:
            case 1:
                try:
                    x=float(input("Enter 1st no. : "))
                    y=float(input("Enter 2nd no. : "))
                    print(x+y)
                    print()
                except ValueError:
                    print("Invalid Input")
                    print()
                except Exception as e:
                    print(e)
                    print()
            case 2:
                try:
                    x=float(input("Enter 1st no. : "))
                    y=float(input("Enter 2nd no. : "))
                    print(x-y)
                    print()
                except ValueError:
                    print("Invalid Input")
                    print()
                except Exception as e:
                    print(e)
                    print()
            case 3:
                try:
                    x=float(input("Enter 1st no. : "))
                    y=float(input("Enter 2nd no. : "))
                    print(x*y)
                    print()
                except ValueError:
                    print("Invalid Input")
                    print()
                except Exception as e:
                    print(e)
                    print()
            case 4:
                try:
                    x=float(input("Enter 1st no. : "))
                    y=float(input("Enter 2nd no. : "))
                    print(x/y)
                    print()
                except ValueError:
                    print("Invalid Input")
                    print()
                except ZeroDivisionError:
                    print("cannot divide by zero")
                    print()
                except Exception as e:
                    print(e)
                    print()
            case 5: exit()
            case _:
                print("Invlid Input. Try again.")
                print()
    except ValueError:
        print("Invalid Input")
        print()
    except Exception as e:
        print(e)
        print()