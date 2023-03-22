# Write a python script to display the current date and time. First create variables to
# store date and time, then display date and time in proper format (like: 13-8-2022 and
# 9:00 PM)
import datetime

# get current date and time
now=datetime.datetime.now()

# formate current date and time
date=now.strftime("%d-%m-%Y")
time=now.strftime("%I:%M %p")

print(date)
print(time)