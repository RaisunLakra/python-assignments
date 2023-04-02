'''
Write a python program to create a function that takes a list and returns a new list
with the original list's unique elements
'''
def convert(lists):
    return list(set(lists))

print(convert([4,5,6,7,7,9,4,5,8]))