'''
Define a function which takes lengths of three sides of a triangle as arguments and
display the perimeter or triangle. Define and apply a decorator which checks for the
validity of the triangle on the basis of lengths of the side. This makes the perimeter to
be displayed when the triangle can exist with the given lengths of the sides
'''
# Decorator - It is a function which takes a function and returns a function

def is_valid(func):
    def wrapper(a,b,c):
        if a+b>c and b+c>a and a+c>b:
            return func(a,b,c)
        else:
            print("Invalid Triangle")
    return wrapper

@is_valid
def perimeter_of_triangle(side1,side2,side3):
    print(side1+side2+side3)

perimeter_of_triangle(4,5,6)
perimeter_of_triangle(3,4,5)
perimeter_of_triangle(2,2,2)
perimeter_of_triangle(1,2,3)