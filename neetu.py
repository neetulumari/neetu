# Wap to swap two mumber
# n1 = int(input("enter the first number "))
# n2 = int(input("enter the second number "))
# temp = n1
# n1 = n2
# n2= temp
# print("the value n1:" , n1)
# print("the value n2:" , n2)
# prime number : if a number having only two factor like 1,19
# n = int(input("enter the number "))
# count = 0
# if n>1:
#     for i in range (1,n+1):
#         if(n%i) == 0:
#             count = count +1
# if count == 2 :
#     print("prime")
# else:
     
#  print("not prime")

# 3. problem 2 practics :WAP TO Which will keep addig string of numbers stops as soon as user presses q on the key board

# sum = 0
# while(True):
#     userInput = input("enter the item price or press q to quit:/n")
#     if(userInput!='q'):
#         sum = sum + int(userInput)
#         print(f"Order so far :{sum}")
#     else:
#         print(f"your bill total is {sum}.Thanks for shoping with us ")
#         break  
# 4. find gratest number among given three number
# a = int(input("enter the first number:"))            
# b = int(input("enter the second  number:"))            
# c = int(input("enter the third  number:"))    
# max = a 
# if max < b :
#   max = b 
# if max <  c:
#     max = c
# print( max)
# a = 11
# b = 7
# if a> b:
#     print("maximum number is ",a)
# else:
#     print("maximum number is ", b)
#7. wap a programme to print tringle shape number  
# n = int(input("enter the number of rows:"))
# for i in range (1, n +1):
#     for j in range (1, i+1):
#         print(i, end = "  " )
#     print()    
# 8 . wap a programme to print star in right angle trinle
# n = int(input("enter the number of rows:"))
# for i in range (1, n +1):
#      for j in range (1, i+1):
#          print("*", end = "  " )
#      print() 
    # wap to find factorial of number  
# import math
# n = int(input("enter the number:"))
# result = math.factorial(n)
# print(result)
#                 ;;;;2nd method
# def fact(n):
#  if n == 0:
#     return 1
#  else:
#     return n*fact(n-1) 

# n = int(input("enter the number :"))  
# result = fact(n)  
# print(result)
# print right angle tringle
# n = int(input("enter the no rows:"))
# for i in range (n):
#     for j in range (i +1):
#         print(i+1 , end = "")
#     print()  
# n = int(input("enter the no rows:"))
# for i in range (n):
#      for j in range (i , -1,-1):
#          print(j+1 , end = "")
#      print() 
# n = int(input("enter the no rows:"))
# for i in range (n):
#      for j in range (i , -1,-1):
#          print(i+1 , end = "")
#      print() 
# n = int(input("enter the no rows:"))
# for i in range (n):
#      for j in range (i , -1,-1):
#          print(n-j , end = "")
#      print() 
n = int(input("enter the no rows:"))
for i in range (n):
     for j in range (i , -1,-1):
         print(j+1 , end = "")
     print() 







