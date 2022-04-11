# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 09:41:08 2018

@author: Magy Gamal
"""
def reverse_list_buggy(L):
    for i in range(len(L)//2):
        j= len(L)-i-1
        temp=L[i]
        L[i]=L[j]
        L[j]=temp
    return L
print(reverse_list_buggy([1,2,3,10]))

def div2(a,b):
    try:
        a=int(a)
        b=int(b)
    except:
        print("not a valid number")
        return 0
    assert b!=0," you gonna divide by zero"
    c=a/b
    print("a/b=",c)
a=input("Enter the first number")
b=input("Enter the second number")
div2(a,b)

import math
def root():
    try:
        a=int(input("Enter a: "))
        b=int(input("Enter b: "))
        c=int(input("Enter c: "))
    except:
        print("not a valid number")
        return 0
    assert a!=0,"not a quadratic equation"
    assert b**2-4*a*c>0," complex conjugate roots"
    x=b**2-4*a*c
    r1=(-b+math.sqrt(x))/(2*a)
    r2=(-b-math.sqrt(x))/(2*a)
    return (r1,r2)
print(root())

 

        


