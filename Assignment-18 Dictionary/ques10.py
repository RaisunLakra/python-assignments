'''
Write a python program to get the key of lowest value from the dictionary.
sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}
'''

sample_dict = {
'C': 92,
'Java': 66,
'Python': 85
}

# min_val=min(val for val in sample_dict.values())
min_val=min(sample_dict.values())
print(min_val)