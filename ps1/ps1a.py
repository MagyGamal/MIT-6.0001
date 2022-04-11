# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:42:33 2018

@author: Magy Gamal
"""
annual_salary=float(input("Enter your annual salary"))
portion_saved=float(input("enter the portion of salary to be saved"))
total_cost=float(input("enter the total cost"))
months=0
current_savings = 0
while current_savings<0.25*total_cost :
     current_savings=current_savings+0.04*current_savings/12+portion_saved*annual_salary/12
     months=months+1
print("Number of months needed is",months)



