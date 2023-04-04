# Create an endless iterator using generator method to produce Prime numbers

def gen():
    def is_prime(p):
        if p==2 or p==3: return True
        for n in range(2,int(p**0.5)+1):
            if p%n==0:
                return False
            return True

    p=2
    while True:
        if is_prime(p):
            yield p
        p+=1

even=gen()
while True:
    choice=input("Enter [y/Y] to get prime otherwise [n/N] for exit : ").lower()
    match choice:
        case 'y':
            print(next(even))
        case 'n':
            break
        case _:
            print("Invalid Input")