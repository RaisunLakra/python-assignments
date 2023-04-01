'''Write a python program to create a function which expects kwargs arguments'''

def fun(**arg):
    for key,val in arg.items():
        print(key,val)
fun(a=1, b=2, c=3)
