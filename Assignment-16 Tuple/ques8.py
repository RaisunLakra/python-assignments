'''
Write a python program to Sort a tuple of tuples by the second item.
tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
'''

# tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))
# for round in range(len(tuple1)):
#     for i in range(len(tuple1)-round):
#         if tuple1[i][1]>tuple1[i+1][1]:
#             a,b=tuple1[i+1],tuple1[i]
#             del tuple1[i],tuple1[i+1]
#             tuple1[i],tuple1[i+1]=b,a
# print(tuple1)

tuple1 = (('a', 21),('b', 37),('c', 11), ('d',29))

for round in range(len(tuple1)):
    for i in range(len(tuple1)-round-1):
        if tuple1[i][1] > tuple1[i+1][1]:
            a, b = tuple1[i+1], tuple1[i]
            tuple1 = tuple1[:i] + (a,) + tuple1[i+1:i+2] + (b,) + tuple1[i+2:]

print(tuple1)