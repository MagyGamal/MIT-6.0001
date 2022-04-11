# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 11:14:47 2018

@author: Magy Gamal
"""

mysum = 0
for i in range(5, 11, 2):
    mysum += i 
    if mysum == 5: 
        break 
    mysum += 1
print(mysum)

hi = "hello there"
name = "ana"
silly = hi + " " + name * 3
print(silly)

pset_time = 15 
sleep_time = 8 
print(sleep_time > pset_time) 
derive = True 
drink = False 
both = drink and derive 
print(both)

s1 = "mit u rock" 
s2 = "i rule mit" 
if len(s1) == len(s2): 
    for char1 in s1: 
        for char2 in s2: 
            if char1 == char2: 
                print("common letter") 
                break
            
def func_a(): 
    print ('inside func_a')
def func_b(y): 
    print ('inside func_b') 
    return y 
def func_c(z): 
    print ('inside func_c') 
    return z() 
print (func_a()) 
print (5 + func_b(2)) 
print (func_c(func_a))

def f(y): 
    x = 1 
    x += 1 
    print(x)
x = 5 
f(x) 
print(x)

def g(y): 
    print(x) 
    print(x + 1)
x = 5 
g(x) 
print(x)

def h(y): 
    x += 1
x = 5 
h(x) 
print(x)

def remove_dups(L1,L2):
    L1_copy = L1[:] 
    for i in L1_copy: 
        if i in L2: 
            L1.remove(i)
    return(L1)
L1 = [1, 2, 3, 4] 
L2 = [1, 2, 5, 6] 
print(remove_dups(L1, L2))

def mult(a, b):
   if b == 1:
       return a
   else:
        return a + mult(a, b-1)
print(mult(2,5))

def fib(x):
   if x == 0 or x == 1:
        return (1)
   else:
        return fib(x-1) + fib(x-2)
print(fib(5))

def fib(n):
  while True:
    if n==0 or n==1:
        return 1
    elif n>1:
        n=(n-1)+(n-2)
    return n
print(fib(5))

