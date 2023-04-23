# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 15:49:12 2022

@author: bruco
"""
def most_frequent(List):
    return max(set(List), key = List.count)

n = int(input())

l = []

for i in range(n):
    l.append(float(input()))
    
moda = most_frequent(l) 
print(f"Number that appears most often = {moda:.2f}")

for i in range(n):
    if l[i] == moda:
        print(f"Position: {i}")