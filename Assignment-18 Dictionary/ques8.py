'''
Write a python program to convert two lists into a dictionary in a way that item from
list1 is the key and item from list2 is the value.
'''

names=["Raunak","Rishi","Meet","Dinesh","Prakhar"]
genders=["male","female","transgender","male","female"]

# my_dic={}
# for i in range(len(names)):
#     my_dic[names[i]]=genders[i]

# my_dic=dict(zip(names,genders))

my_dic={names[i]:genders[i] for i in range(len(names))}

print(my_dic,type(my_dic))
print("\n\n")
dic=my_dic.items()
print(type(dic))