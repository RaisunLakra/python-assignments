"""
Write a Python script to print distinct elements along with their frequencies of
occurrence in the list.
"""
mylist=[2,3,'type',True,True,False,True,3,4,2,0.5,7,0.5,'type']

newlist=[]

for i in range(len(mylist)):
    if mylist[i] in [item[0] for item in newlist]:
        newlist[[item[0] for item in newlist].index(mylist[i])][1]+=1
    else:
        newlist.append([mylist[i],1])

print(newlist)