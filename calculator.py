number1=float(input("Enter a number:"))
number2=float(input("Enter a number:"))
add=number1+number2
div=number1/ number2
multi=number1* number2
subs=number1- number2
Click=input("Enter the operation:")

if Click=="+":
    print("The addition is:",add)
elif Click=="*":
    print("The multiplication is:",multi)
elif Click=="/":
    print("The division is:",div)
elif Click=="-":
    print("The substraction is:",subs)
else:
    print('You are a bokac**da')    
