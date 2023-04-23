# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:57:23 2022

@author: bruco
"""
n = int(input("Number of rows ="))
m = int(input("Number of columns ="))

a = [[0] * m for i in range(n)]

for i in range (n):
    for j in range(m):
        a[i][j]= int(input(f"matrix[{i}][{j}]="))

l = []
s = 0.0 

for i in range (n):
    for j in range(m):
        s = s + a[i][j]
    l.append(s/m)
    s = 0.0 

        
print(l)
