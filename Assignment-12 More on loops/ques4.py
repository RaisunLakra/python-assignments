"""
Write a python script to print all Prime numbers between two given numbers (both
values inclusive)
"""

x=int(input("Enter a no. : "))
y=int(input("Enter another no. : "))

for num in range(x,y+1):
    if num<2:
        continue
    else:
        flag=1
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                flag=0
                break
        if flag==1:
            print(num,end=" ")