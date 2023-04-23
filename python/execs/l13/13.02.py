# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:05:01 2022

@author: bruco
"""

def average(l):
    s = 0
    for i in l :
        s = s + i
    return float(s/len(l))
    

n = int(input("Number of elements of list ="))

l = []

for i in range(n):
    l.append(int(input(f"l[{i}]=")))

print("Average =",average(l))
    
