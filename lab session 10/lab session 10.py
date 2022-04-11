# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 09:06:59 2018

@author: Magy Gamal
"""
import time
import random
def generate_list(length):
    L=[]
    for i in range(length):
        L.append(random.randint(1,1000))
    return L
#1
def search(L,e):
   for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
   return False

#testList=[1,3,4,5,9,18,27]
testList=generate_list(1000000)
#testList=generate_list(1000)
starting_time=time.clock()
print(search(testList,5))
ending_time=time.clock()
total_time=ending_time-starting_time
print("Execution time is",total_time)
2
def isSubset(L1,L2):
    for e1 in L1:
        matched=False
        print("o")
        for e2 in L2:
            if e1==e2:
                matched=True
                break
        if not matched:
            return False
    return True
testSet1=[1,2,3,4,5]
testSet2=[1,2,3,4]

#testSet=[1,6]
starting_time=time.clock()
print(isSubset(testSet1,testSet2))
ending_time=time.clock()
total_time=ending_time-starting_time
print("Execution time is",total_time)

#3 
def intersect(L1,L2):
    tmp=[]
    for e1 in L1:
        for e2 in L2:
            if e1==e2:
                tmp.append(e1)
    res=[]
    for e in tmp:
        if not(e in res):
            res.append(e)
    return res
testSet1=[1,2,3,4,5]
testSet2=[1,2,3,4]

starting_time=time.clock()
print(intersect(testSet1,testSet2))
ending_time=time.clock()
total_time=ending_time-starting_time
print("Execution time is",total_time)

def generate_list(length):
    L=[]
    for i in range(length):
        L.append(random.randint(1,1000))
    return L
def search(L,e):
   for i in range(len(L)):
        if L[i]==e:
            return True
        if L[i]>e:
            return False
   return False

sizes=[10,100,1000,10000,1000000]
times=[]
for i in sizes:
    L=generate_list(i)
    starting_time=time.clock()
    search(L,10000001)
    ending_time=time.clock()
    total_time=ending_time-starting_time
    times.append(total_time)
    

    
def plot(sizes, times):
     import matplotlib.pyplot as plt 
     plt.figure()
     plt.plot(sizes, times)
     plt.xlabel("Sizes")
     plt.ylabel("Times(s)")
     plt.grid(True, which="both")
     plt.show() 
plot(sizes,times)

            
