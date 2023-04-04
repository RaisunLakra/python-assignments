# Use iter and next method to access all the elements of a given set using while loop
s={1,2,4,5,5}

it=iter(s)
while True:
    try:
        print(next(it))
    except StopIteration:
        break