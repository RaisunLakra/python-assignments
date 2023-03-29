# Write a python script to calculate HCF of two numbers
def hcf(a,b):
    if b==0:
        return a
    else:
        return hcf(b,a%b)

a,b=map(int,input("Enter two no. using space : ").split())
print(hcf(a,b))