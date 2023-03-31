'''
Write a python program to print the value 20 from given nested tuple
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))
'''
tuple1 = ("Python", [10, 20, 30], (2, 4, 16))

for e in tuple1:
    try:
        if 20 in e:
            print('20')
    except TypeError:
        continue