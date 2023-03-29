# Write a python script to calculate LCM of two numbers

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

print("Enter two no.")
num1=int(input("1st no. "))
num2=int(input("2nd no. "))

lcm=num1*num2//gcd(num1,num2)

print(lcm)