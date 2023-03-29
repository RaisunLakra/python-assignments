#  Write a python script to check whether a given number is Prime or not

num=int(input("Enter a given no. : "))
if num<2:
    print("Not a prime no.")
else:
    flag=1
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            flag=0
            print("Not a prime no.")
            break
    if flag==1:
        print("Prime No.")