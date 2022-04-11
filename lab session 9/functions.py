# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 09:49:02 2018

@author: Magy Gamal
"""
#1
def Max3(x,y,z):
    if x>y and x>z:
        print("maximum  of the three numbers is:",x)
        return(x)
    elif y>z and y>x:
        print("maximum of the three numbers is:",y)
        return(y)
    else:
        print("maximum of the three numbers is:",z)   
        return(z)
x=input("please enter the first number")
while not(x.isnumeric()):
    x=input("please enter the first number only numbers are permitted")
x=float(x)
y=input("please enter the second number")
while not(y.isnumeric()):
    y=input("please enter the first number only numbers are permitted")
y=float(y)
z=input("please enter the third number")
while not(z.isnumeric()):
    z=input("please enter the first number only numbers are permitted")
z=float(z)
Max3(x,y,z)
#2
def Sum_of_list(x):


    
    