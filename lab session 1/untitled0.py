# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 09:36:27 2019

@author: Magy Gamal
"""
def genSubsets(s): 
    if len(s) == 0:
        return [[]]
    smaller = genSubsets(s[:-1])
    extra = s[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller+new
print(genSubsets("abc"))
