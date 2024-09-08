"""we can modify tuple converting  into list bcs list is mutable """
tup=(1,2,3,4,5)
listtup=list(tup)

listtup.append(7)   #we add a 7 at last position
listtup.pop(1)      #we delete the value which is at index 1
tup=tuple(listtup)
print(tup)

"""similarly we can do other operations"""