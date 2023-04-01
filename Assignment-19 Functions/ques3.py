'''
Write a python program to create a function which expects an unknown number of
arguments
'''

def fun_arg(*arg):
    print(arg)
    # print(type(arg))

fun_arg(1,2,3,4,5)