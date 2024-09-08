import time
b=time.strftime('%H:%M:%S')
print(b)

a=int(time.strftime('%H'))
# import random
# a=random.randint(1,24)
# print(a)
if 5< a <12:
    print("Good Morning")
if  a==12:
    print("Good Noon ")
if 12< a <18:
    print("Good Afternoon")
if 18< a <21:
    print("Good Evening")
if 21< a <=24:
    print("Good Night")
if 1< a <5:
    print("Good Night")




    