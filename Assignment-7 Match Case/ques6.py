# Write a python program to check whether a given string is a multiword string or single
# word string using match case statement
str=input("Enter a string : ")
is_space=True if ' ' in str else False
match is_space:
    case True:
        print("Multiword String")
    case False:
        print("Single Word String")