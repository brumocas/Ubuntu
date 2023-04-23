# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:44:23 2022

@author: bruco
"""

n = int (input())

a = str(n % 10)

n = int( n/10)

b = str(n % 10)

n =int(n/10)

c =str(n % 10) 


print("Numbers:")
print(c+b+a)
print(c+a+b)
print(b+a+c)
print(b+c+a)
print(a+b+c)
print(a+c+b)
 