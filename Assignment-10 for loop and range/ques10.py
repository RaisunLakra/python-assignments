"""
Write a python script to display all prime numbers within a range.
# range
start = 15
end = 45
"""
for num in range(15,46):
    flag=1
    for i in range(int(num**0.5),1,-1):
        if num%i==0:
            flag=0
            break
        else:
            flag=1
    if flag==1:
        print(num)