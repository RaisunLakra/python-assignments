# Create a generator to produce first n terms of Fibonacci series

def gen(num):
    a,b=0,1
    for i in range(0,num):
        yield a
        a,b=b,a+b

it = gen(12)
while True:
    try:
        print(next(it))
    except StopIteration:
        break