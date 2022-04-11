# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 09:04:08 2018

@author: Magy Gamal
""" 
#1 solved at home
def factor(x,i):
    y=[]
    if i==1:
        y=[1]
        return y
    elif x%i==0:
        y.append(i)
    return (factor(x,i-1))+y
print(factor(30,30))     
#3
def power(x,y):
    if y==1:
        return x
    else:
       return x* power(x,y-1)
x=int(input("please enter the first number"))
y=int(input("please enter the second number"))
print(power(x,y))

#4.1
grade_1={"Id_1":100,"Id_2":75,"Id_3":300}
grade_2={"Id_1":300,"Id_2":50,"Id_4":400,"Id_5":150}
grade_union= grade_1
for i in grade_2:
    if i in grade_1:
        grade_union[i]=grade_1[i]+grade_2[i]
    else:
        grade_union[i]=grade_2[i]
print(grade_union)
#4.2 solved at home
def max3(grade):
    for i in grade:
        return print("maximum_first=",(i,max(grade[i]))
grade = {"Id_1": 400, "Id_2": 125,"Id_4": 500, "Id_3": 300,"Id_5":150}
print(max3(grade))       
#4.3 solved at home
def exceed(grade):
    for i in grade:
        if grade[i] > 200:
            x=print(i,"passed")
        else:
            x=print(i,"not passed") 
    return x
grade = {"Id_1": 400, "Id_2": 125,"Id_4": 400, "Id_3": 300,"Id_5":150} 
print(exceed(grade))
#5 solved at home
def frequency(words):
    freq={}
    for x in words:
        freq[x]=freq.get(x,0)+1
    return freq
y=input("please enter a sentence")
print(frequency(y))