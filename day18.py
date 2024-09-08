# i=1
# while i<=5:
#     print(i)
#     i+=1

# i=1
# while i<=6:
#     print(f"i={i}")
#     i+=1
# print('Out of the loop')

# j=1
# while j<=5:
#      k=1
#      while k<=3:
#         print(f"j={j},k={k}") #for every iretation of  outer loop the inner loops iretate until the condition will become false
#         k+=1
#      j+=1


# j=1
# while j<=5:
#      k=1
#      print('sakib') #sakib will print for every iteration of outer loop then it will go for inner loop
#      while k<=3:
#         print(f"j={j},k={k}") #for every iretation of  outer loop the inner loops iretate until the condition will become false
#         k+=1
#      j+=1
        
# i=1
# sum=0
# while i<=7:
#     print(i,end=" ")
#     sum+=i
#     i+=1
# print("\nThe sum of the numbers:",sum)    

# a,b=0,1
# count=0
# while count<10:
#     print(a)
#     count+=1
#     a,b=b,a+b
# number=0
# while number<=0:
#   number=int(input('Enter a number:'))
# print(f"You entered positive number {number}")  

# import random
# target=random.randint(1,5)
# guess=None
# while guess !=target:
#     guess=int(input("Enter a number:"))
#     if guess>target:
#         print(f"You guessed high because target is {target} but you guessed {guess} ")
#     elif guess<target: 
#         print(f"You guessed low because target is {target} but you guessed {guess} ")
# print(f"You guessed it because target is {target} and you guessed {guess}")        

    
# num=int(input("Enter a positive integer:"))
# a=(num)
# rev_num=0
# while num>0:
#     digit=num%10
#     rev_num=rev_num*10+digit    
#     num//=10
    
# print(f"The reverse of the number {a} is {rev_num}")    

# fruits=["mango","apple","lichee"]
# i=0
# while i<len(fruits):
#     fruits[i]=fruits[i].upper()
#     i+=1
# print(fruits)

nums=[4,5,6,7,3,2]
target=int(input("Enter a number from the list:"))
i=0
while i<len(nums):
    if target==nums[i]:
        print(f"The number is found at index {i}")
        break
    i+=1
else:
    print("The number is not found at index")    
  


