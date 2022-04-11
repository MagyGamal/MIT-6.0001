# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 09:10:41 2018

@author: Magy Gamal
"""
import time
import random 
def plot(sizes, times):    
    import matplotlib.pyplot as plt    
    plt.figure()    
    plt.plot(sizes, times)    
    plt.xlabel("Sizes")    
    plt.ylabel("Times(s)")    
    plt.grid(True, which="both")    
    plt.show()
def generate_list(length):    
    L = []    
    for i in range(length):        
        L.append(random.randint(1,1000))    
        return L
#1
def someFunction(x,y):    
    return x*y
t = [] 
s = []
time_start = time.clock() 
for i in range(5,3000):    
        
    someFunction(i, i)    
    time_end = time.clock() - time_start    
    t.append(time_end)    
    s.append(i) 
plot(s,t)

#2
def bisect_search(L, e):    
    def bisect_search_helper(L, e, low, high):        
        print('low: ' + str(low) + '; high: ' + str(high))  #added to visualize        
        if high == low:            
            return L[low] == e        
        mid = (low + high)//2        
        if L[mid] == e:            
            return True        
        elif L[mid] > e:            
            if low == mid: #nothing left to search                
                return False            
            else:                
                return bisect_search_helper(L, e, low, mid - 1)        
        else:            
            return bisect_search_helper(L, e, mid + 1, high)    
    if len(L) == 0:        
            return False    
    else:        
            return bisect_search_helper(L, e, 0, len(L) - 1)
t = [] 
s = []
time_start = time.clock() 
for i in range(1, 7):    
    L = generate_list(10**i)    
    L.sort()        
    bisect_search(L, 1)    
    time_end = time.clock() - time_start    
    t.append(time_end)    
    s.append(len(L))
plot(s,t)
#3
def linear_search(L, e):    
    found = False    
    for i in range(len(L)):        
        if e == L[i]:            
            found = True    
    return found 
t = [] 
s = []
time_start = time.clock()
for i in range(1, 5):    
    L = generate_list(10**i)    
         
    linear_search(L, 1)    
    time_end = time.clock() - time_start    
    t.append(time_end)    
    s.append(len(L)) 
plot(s,t)

##4
def bubbleSort(L):   
    for i in range(len(L)):              
        for j in  range(len(L)-i-1): 
            #   Last i elements are already in place           
            if L[j] > L[j+1]:               
                tmp = L[j]               
                L[j] = L[j+1]               
                L[j+1] = tmp
time_start = time.clock()   
for i in range(1, 5):    
    L = generate_list(10**i)    
     
    bubbleSort(L)    
    time_end = time.clock() - time_start    
    t.append(time_end)    
    s.append(i) 
plot(s,t)
#5
def fibonacci(n):    
    if n <= 2:        
        return 1    
    else:        
        return fibonacci(n-1) + fibonacci(n-2) 
t = [] 
s = []
time_start = time.clock() 
for i in range(5, 25):    
            
    fibonacci(i)    
    time_end = time.clock() - time_start    
    t.append(time_end)    
    s.append(i) 
plot(s,t)
##
#    
#
