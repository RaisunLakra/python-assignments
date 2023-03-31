'''Write a python program to check if all items in the tuple are the same'''
a=(1,1,1)
print("Yes" if all(x==a[0] for x in a) else "No")

b=(2,4,6,6)
print("Yes" if all(x==b[0] for x in b) else "No")

# for e in a:
#     flag=1
#     if e!=a[0]:
#         flag=0
#         break
# print("Yes")if flag==1 else "No"

# for e in b:
#     flag=1
#     if e!=b[0]:
#         flag=0
#         break
# print("Yes" if flag==1 else "No")