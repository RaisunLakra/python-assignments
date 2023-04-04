# Create an endless iterator using generator method to produce terms of Fibonacci
# series

def gen():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

n=gen()
while True:
    choice=input("Enter [y/Y] to get fibonacci otherwise [n/N] for exit : ").lower()
    match choice:
        case 'y':
            print(next(n))
        case 'n':
            break
        case _:
            print("Invalid Input")