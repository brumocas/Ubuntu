# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 17:28:48 2022

@author: bruco
"""

n = int(input())

negative = 0
positive = 0

for i in range(n) :
    x = float(input())
    if x > 0:
        positive = positive + 1
    else :
        negative = negative + 1     
        
        
nper = 100 * negative / n 
pper = 100 * positive / n 

print(f"% positive values = {pper:.1f}%")
print(f"% negative values = {nper:.1f}%")
         
         
        


