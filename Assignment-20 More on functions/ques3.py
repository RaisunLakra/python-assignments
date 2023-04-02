'''
Write a python program to create a function that prints the even numbers from a
given list.
Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
'''

def findeven(nums):
    for list in nums:
        if list%2==0:print(list)

findeven([1, 2, 3, 4, 5, 6, 7, 8, 9])