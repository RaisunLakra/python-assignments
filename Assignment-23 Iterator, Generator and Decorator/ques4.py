# Create a generator to produce squares of first N natural numbers

def gen(num):
    for n in range(1,num+1):
        yield n**2

it = gen(5)
while True:
    try:
        print(next(it))
    except StopIteration:
        break