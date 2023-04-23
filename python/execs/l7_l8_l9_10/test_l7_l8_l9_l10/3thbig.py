# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 11:04:47 2022

@author: bruco
"""

n1 = int(input("Number of elements in the list ="))


l1 = []

for i in range(n1):
    l1.append(int(input(f"l[{i}]=")
    
nth = int(input("Number of greatest elements ="))
  
l1.sort()

l1.reverse()

print()

print(l1[:nth])




