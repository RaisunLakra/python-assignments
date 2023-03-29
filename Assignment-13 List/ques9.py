# Write a Python script to create a list of city names taken from the user.

city=[]
while True:
    print("Enter your choice:")
    print("1. Add city")
    print("2. Print choice")
    print("3. Delete from last")
    print("Enter any keyword to exit")
    try:
        choice=int(input())
    except ValueError:
        exit()
    match(choice):
        case 1:
            city.append(input("Enter city : "))
        case 2:
            print(city)
        case 3:
            try:
                city.remove(city[-1])
            except IndexError:
                print("list is empty")
        case _:
            exit()