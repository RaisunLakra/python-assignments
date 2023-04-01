'''
Write a python program to merge two python dictionaries into one dictionary.
'''

student={"name":"Raunak Chauhan"} # dictionary is not hashable but there elements are hashable
gender={"gender":"female"}

mca_girl=student|gender

print(mca_girl)