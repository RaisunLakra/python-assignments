'''
Write a python program to add elements of list to a set
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
'''

thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]

# thisset.add(mylist) # TypeError: unhashable type: 'list'
thisset.update(mylist)
print(thisset)