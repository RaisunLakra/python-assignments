'''
Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)
'''

tuple1 = (11, [22, 33], 44, 55)

for i in range(len(tuple1)):
    try:
        if 22 in tuple1[i]:
            tuple1[i][tuple1[i].index(22)]=222
            break
    except TypeError:
        continue

print(tuple1)