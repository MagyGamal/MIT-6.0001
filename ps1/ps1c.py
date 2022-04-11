# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 09:23:54 2018

@author: Magy Gamal
"""
annual_salary=float(input("Enter your starting salary:"))
semi_annual_raise=0.07
r=0.04
total_cost=1000000
portion_down_payment=0.25
current_savings=0
step=0
low=0
high=10000
guess=((high+low)/2)
while abs(current_savings-portion_down_payment*total_cost)>=100:
     for month in range (36) :
        if month %6 == 0:
             annual_salary=annual_salary+semi_annual_raise*annual_salary
     current_savings=current_savings+r*current_savings/12
     if current_savings<portion_down_payment*total_cost:
         guess=low
     else:
         guess=high
     step+=1
     rate=guess/1000    
print("best savings rate is:",rate)
print("steps in bisection:",step)
   
         
    