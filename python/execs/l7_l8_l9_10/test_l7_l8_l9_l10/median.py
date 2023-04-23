# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:14:43 2022

@author: bruco
"""

n = int(input())

l = []

for i in range(n):
    l.append(int(input()))
    
l.sort()

m = float(n/2) - 0.5

median = float ((l[int(m)] ))

print(f"Median = {median:.2f}")