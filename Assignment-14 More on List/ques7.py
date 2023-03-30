# Write a Python script to remove all non int values from a list.

mylist=['helo',1,3,5,'the',0.8,True,False]

i=0

while i < len(mylist):
    if type(mylist[i])!=int: # if not isinstance(mylist[i],int):
        del mylist[i]
    else:
        i+=1
print(mylist)