"""
Write a python script to Change the values "SQL" and "Reactnative" with the values
"NoSQL" and "Flutter" (List is thislist = ["Java", "SQL", "C", "Reactnative",
"Javascript", "Python"]
"""

list = ["Java", "SQL", "C", "Reactnative",
        "Javascript", "Python"]
print(list)

# Replace first SQL and reactnative
try:
    list[list.index("SQL")]="NoSQL"
except ValueError:
    print("no SQL in the list")

try:
    list[list.index("Reactnative")]="Flutter"
except ValueError:
    print("Reactnative does not exist.")

print(list,end="\n\n")

list = ["Java", "SQL", "C", "Reactnative",
        "Javascript", "SQL", "Python", "Reactnative", "SQL", "Reactnative"]

print(list)
# to reamove change every SQL to NoSQL and Reactnative to Flutter
for x in list:
    if x=="SQL":
        list[list.index(x)]="NoSQL"
    if x=="Reactnative":
        list[list.index(x)]="Flutter"

print(list)