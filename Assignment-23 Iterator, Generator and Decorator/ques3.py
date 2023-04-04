# Create a generator to produce first n even natural numbers
def gen(num):
    for i in range(1,num+1):
        yield 2*i

# print([n for n in gen(10)])

# wrong code
# while True:
#     try:
#         print(next(gen(10))) # this will give error because we are calling gen() infinite time which creates generator object but does not store the object any where
#     except StopIteration:
#         break

gn=gen(10)
while True:
    try:
        print(next(gn)) # this will give error because we are calling gen() infinite time which creates generator object but does not store the object any where
    except StopIteration:
        break