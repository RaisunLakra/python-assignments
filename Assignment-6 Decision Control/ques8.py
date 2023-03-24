# Write a python script to check whether a given quadratic equation has two real &
# distinct roots, real & equal roots or imaginary roots
print("Quadratic Equation : ax2 + bx + c")
a=int(input("Enter a of quadratic equation : "))
b=int(input("Enter b of quadratic equation : "))
c=int(input("Enter c of qudratic equation : "))
def find(a,b,c):
    d=b**2-4*a*c
    if d==0:
        print("equal root")
    elif d>0:
        print("two distinct root")
    else:
        print("imaginary root")
find(a,b,c)