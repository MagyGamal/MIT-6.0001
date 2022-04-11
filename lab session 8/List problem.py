# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 09:11:57 2018

@author: Magy Gamal
"""
Cdegrees=[-20,-15,-10,-5,0,5,10,15,20,25,30,35,40]
Fdegrees=[]
for x in Cdegrees:
    F=(9.0/5)*x+32
    Fdegrees.append(F)
print(Fdegrees)

import math
X=[]
sum=0
N=5
for i in range(N):
    X.append(int(input("Enter a number")))
    sum+=X[i]
Average=sum/N
print("Average=",Average)
#Standard Deviation
sum=0
for i in range(N):
    sum+=(X[i]-Average)**2
SD=math.sqrt(sum/(N-1))
print("Strandard Deviation=",SD)




    
    
    
    
    