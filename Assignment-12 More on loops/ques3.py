# Write a python script to print all Prime numbers under 100
for num in range(1,101):
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