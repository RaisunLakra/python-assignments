'''
Write a python program to add items from another set to the current set. thisset =
{"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}
'''

thisset = {"Java", "Python", "SQL"}
secondset= {"C", "Cpp", "NoSQL"}

# thisset.add(secondset) # TypeError : unhashable type: 'set'
thisset.update(secondset) # Output : {'Java', 'NoSQL', 'SQL', 'Python', 'Cpp', 'C'}
print(thisset)