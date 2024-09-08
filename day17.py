# x="SAKIB"
# for i in x:
#     print(i,end=" ")
# x=range
# for i in x(1,100,2):
#     print(i)    

# for a in range(1,200,2):
#     print(a)

# fruits=["Mango","Lichee","Guava","Apple"]
# for j in fruits:    
#     print(j)
#     for l in j:
#         print(l)

# a=int(input("Enter the starting number:"))
# b=int(input("Enter the ending number:"))
# c=int(input("Enter the increment betn numbers:"))

# sum=0
# for i in range(a,b+1,c):
#     sum +=i
#     print(i,end=" ")

# print("\nThe sum of the numbers is:",sum)    

# num=(input("Enter a character: "))
# for digit in num[::-1]:
#     print(digit,end="")


import random
target=random.randint(1,5)
guess=int(input("Enter an integer:"))
for x in range(guess):
    if guess==target:
        print("You won")
        break
else:
    print(f"You lost because target was {target} and you guessed {guess}")        
    
