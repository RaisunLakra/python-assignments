# Write a recursive python function to print cubes of first N natural numbers
def cube(num):
    if num>0:
        cube(num-1)
        print(num**3)

cube(7)