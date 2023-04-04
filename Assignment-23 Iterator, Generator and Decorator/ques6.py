#  Create a generator to produce first n prime numbers

def gen(num):
    def is_prime(p):
        if p==2 or p==3: return True
        for n in range(2,int(p**0.5)+1):
            if p%n==0:
                return False
            return True
    i=1
    p=2
    while i <= num:
        if is_prime(p):
            yield p
            p+=1
            i+=1
        else:
            p+=1

even=gen(10)
while True:
    try:
        print(next(even))
    except StopIteration:
        break