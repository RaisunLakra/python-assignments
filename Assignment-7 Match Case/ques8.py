"""
Write a python script to check whether two given strings are identical, first string
comes before the second in dictionary order or first string comes after the second
string in dictionary order using match case statement
"""

str1=input("Enter a string : ")
str2=input("Enter another string : ")
match str:
    case n if str1==str2:
        print("Identical")
    case n if str1<str2:
        print(f"{str1} comes before {str2}")
    case _:
        print("%s comes after %s"%(str1,str2))