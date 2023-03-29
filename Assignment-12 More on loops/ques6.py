# Write a python script to print first N prime numbers

n=int(input("Enter a no. : "))

num=2
for i in range(0,n):
    while True:
        flag=1
        for j in range(2,int(num**0.5)+1):
            if num%j==0:
                flag=0
                break
        if flag==1:
            print(num)
            break
        num+=1
    num+=1