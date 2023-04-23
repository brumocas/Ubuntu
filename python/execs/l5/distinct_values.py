# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:44:52 2022

@author: bruco
"""

n = int(input())


l = []

for i in range(n):
    l.append(float(input()))
    
s = set(l)

lenght = len(s)

print(f"number of distinct values: {lenght}")