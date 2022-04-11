# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 09:12:02 2018

@author: Magy Gamal
"""
class Coordinate(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __str__(self):
        return "<"+str(self.x)+","+str(self.y)+">"
    def distance(self,other):
        x_diff_sq=(self.x-other.x)**2
        y_diff_sq=(self.y-other.y)**2
        return (x_diff_sq+y_diff_sq)**0.5
c=Coordinate(3,4)
origin=Coordinate(0,0)
print(c.x,origin.x)
print(c.distance(origin))
print(Coordinate.distance(c,origin))
print(origin.distance(c))
print(c)

class Fraction(object):    
    """    Rational Numbers with support for arithmetic operations.        >>> a = Fraction(1, 2)        >>> b = Fraction(1, 3)        >>> print(a + b)        5/6        >>> print(a – b)        1/6        >>>print( a * b)        1/6        >>>print( a/b)        3/2    """
    def __init__(self, num, denom):
        self.num=num
        self.denom=denom
    def __str__(self):     
        """ Retunrs a string representation of self """ 
        return "<"+str(self.num)+","+str(self.denom)+">"
    def __add__(self, other): 
        """ Returns a new fraction representing the addition """     
        top = self.num*other.denom + self.denom*other.num     
        bott = self.denom*other.denom    
        return Fraction(top, bott) 
    def __sub__(self, other): 
        """ Returns a new fraction representing the subtraction """
        top_1=self.num*other.denom-self.denom*other.num
        bott_1=self.denom*other.denom
        return Fraction(top_1,bott_1)
    def __mul__(self, other):
        top_2=self.num*other.num
        bott_2=self.denom*other.denom
        return Fraction(top_2,bott_2)
    def __float__(self): 
        """ Returns a float value of the fraction """     
        return self.num/self.denom 
    def inverse(self): 
        """ Returns a new fraction representing 1/self """
        return Fraction(self.denom,self.num)
    def __truediv__(self,other):
        top=self.num*other.denom
        bott=self.denom*other.num
        return Fraction(top,bott)
 
    def division (self,other):
        top=self.num*other.denom
        bott=self.denom*other.num
        print("new function")
        return Fraction(top,bott)
    
a = Fraction(1,4)
b = Fraction(3,4)
c = a + b 
# c is a Fraction object
print(c)
print(float(c))
print(Fraction.__float__(c))
print(float(b.inverse())) 
c = Fraction(3.14, 2.7) 
print(a*b)
print(a/b)

print(Fraction.division(a,b))


class intSet(object):
    """    An intSet is a set of integers    The value is represented by a list of ints, self.vals    Each int in the set occurs in self.vals exactly once          """
    def __init__(self):
        """ Create an empty set of integers """
        self.vals = []
    def insert(self, e):
        """ Assumes e is an integer and inserts e into self """
        if not e in self.vals:
            self.vals.append(e)
    def member(self, e):
               """ Assumes e is an integer                         Returns True if e is in self, and False otherwise   """
               return e in self.vals
    def remove(self, e):
        """         Assumes e is an integer and removes e from self              Raises ValueError if e is not in self """
        try:
            self.vals.remove(e)
        except:
            raise  ValueError(str(e) + ' not found')
    def __str__(self):
        """ Returns a string representation of self """
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
s = intSet()
print(s)
s.insert(3)
s.insert(4)
s.insert(3)
print(s)
s.member(3)
s.member(5)
s.insert(6)
print(s) 
s.remove(3)
# leads to an error
print(s)
s.remove(3)
 


    