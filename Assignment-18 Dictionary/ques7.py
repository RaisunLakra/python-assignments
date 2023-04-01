'''
Write a python program to create three dictionaries, then create one dictionary that
will contain the other three dictionaries.
'''

person1={"name":"Raisun Lakra","age":25,"gender":"male"}
person2={"name":"Roshni Lakra","age":28,"gender":"female"}
person3={"name":"Rajender Tigga","age":37,"gender":"male"}

people={"House_owner":person1,"Buyer":person2,"Contractor":person3}

print(people)