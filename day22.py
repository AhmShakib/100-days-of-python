hudai=["food",True,"jame",4,5,"sakib"]
# print(hudai)
# print(hudai[3])
# print(hudai[len(hudai)-1])

# if "food" in hudai:
#     print("Yes")
# else:
#     print("No")    

# if "flo" in "food":
#     print("YES")
# else:
#     print('No') 
   
# for x in hudai:
#     print(x)

# for x in hudai:
#     print(x)


"""list comprehension : it creates list from other iterables like list,tuples,array,dic etc
syntax=[item for item in iterable if condition]"""

lst=[i for i in range(1,10)] 
print(lst) 
lst2=[i*i for i in range(1,5)]
print(lst2)

names=["Sakib","Hasnat","Abdullah","Shoyeb","Kafil","Sujon"]  
namewiths=[item for item in names if "S" in item ] #whic has capital S
print(namewiths)