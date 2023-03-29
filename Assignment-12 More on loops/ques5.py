# Write a python script to find next prime number of a given number
n=int(input("Enter a no. : "))
num=n+1

while True:
    if num<2:
        continue
    else:
        flag=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                flag=0
                break
        if flag==1:
            print(num)
            break
        num+=1