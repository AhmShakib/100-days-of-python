#case match the word serially if the first condition doesn't match it will go for 2nd one that's why case use for making swicth
x=int(input("Enter any num:"))
match x:
    case 0:
        print("number is zero")
    case 4:
          print("Number is four")
    case _ if x!=20:
          print(x,"number is not 20")
    case _ if x!=30:
          print(x,"number is not 30")
          
 
    