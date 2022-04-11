# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:00:34 2018

@author: Magy Gamal
"""

annual_salary=float(input("Enter your annual salary"))
portion_saved=float(input("Enter the portion of salary to be saved"))
total_cost=float(input("Enter the total cost"))
semi_annual_raise=float(input("Enter your semi annual rasie"))
current_savings=0
x=int(0)
while current_savings<0.25*total_cost :
     current_savings=current_savings+0.04*current_savings/12+portion_saved*annual_salary/12
     x=x+1
     if x % 6 == 0:
         annual_salary=annual_salary+semi_annual_raise*annual_salary
     else:
         annual_salary=annual_salary
print("Number of months needed is",x)