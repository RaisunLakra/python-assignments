# Create a generator to produce first n odd natural numbers

def gen(num):
    for n in range(1,num+1):
        yield 2*n-1

print([n for n in gen(10)])