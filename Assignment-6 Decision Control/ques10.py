# Write a python script to print greater among three numbers. Print number only once
# even if the numbers are the same.
a=int(input("Enter 1st no : "))
b=int(input("Enter 2nd no : "))
c=int(input("Enter 3rd no : "))

def compare(a,b,c):
    if a>b:
        if a>c:
            print("%d is greater than %d and %d"%(a,b,c))
        else:
            print("%d is greater"%c)
    elif b>c:
        print(f"{b} is greater than {a} and {c}")
    else:
        print(f"{c:d} is greater than {a:d} and {b:d}")
compare(a,b,c)