# Write a python script to accept one complex number from the user and display the
# greater number between real part and imaginary part
x=complex(input("Enter complex no : "))
if x.real > x.imag:
    print(f"{x.real} is greater than {x.imag}")
else:
    print(f"{x.imag} is greater than {x.real}")