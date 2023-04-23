# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:25:04 2022

@author: bruco
"""

n = int(input())
add = 0

for i in range(0, n):
    a = float(input())
    add = add + a
    
mean=add/n
print(f"Arithmetic mean = {mean:.2f}")    
    