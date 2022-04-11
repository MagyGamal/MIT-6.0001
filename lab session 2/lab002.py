# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
print("ASCII Art")
print("Enter square to draw a square and triangle to draw a triangle.")
choice=input("[square/triangle]:")
if choice =="square":
    print("*"*14)
    print("*"," "*10,"*")
    print("*"," "*10,"*")
    print("*"," "*10,"*")
    print("*"*14)
elif choice =="triangle":
    print("*")
    print("* *")
    print("* * *")
    print("* * * *")
    print("* * *")
    print("* *")
    print("*")
else:
    print("invalid choice.")
    
import numpy
print("Enter your ID If your ID is odd ID it will perform exponentiation and Even ID will perform the logarithm of a number.")
choice=int(input("01201700"+"[%2==1/%2==0]:"))
if choice %2 == 1:
    x=input("Enter the base x:")
    y=input("Enter the exponent y:")
    z=float(x)**float(y)
    print(z)
elif choice %2 == 0:
    x=input("Enter the number:")
    x=float(x)
    z=numpy.log2(x) 
    print("log2 of the number is:",z)
    #I changed the title and to obligate the user to enter his ID i wrote the common part between quotation marks to be printed as it is and told him to write the rest of the number if it is divided by 2 and the remainder is 1 then  it is odd and he will perform exponentiation if the remainder is 0 then it is even
    
print("loop-powered shapes I")
baselength=input("Enter the length of the base of the triangle:")    
baselength=int(baselength)
i=0
while i < baselength+1:
    if i %2 == 1:
       print(i*"^")
       i=i+1
    elif i%2==0:
       print(i*"$")
       i=i+1
        
height=input("Enter the height of the square:")     
height=int(height)
print("*"*14)
i=0
while i < height-2:
    print("*"," "*10,"*")
    i=i+1
print("*"*14)

import random
user=int(input("Enter a number between 1 and 10"))
computerguess=random.randint(1,10)
if user >= 1 and user <= 10:
    while user!=computerguess:
        user=int(input("Enter a number between 1 and 10"))
        import random
        computerguess=random.randint(1,10)
    print("your guess has matched the computer guess")
else:
    print("your guess isnot in the range")
        
        




        

        
  

    