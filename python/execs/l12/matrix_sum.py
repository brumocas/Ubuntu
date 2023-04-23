# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:28:15 2022

@author: bruco
"""

n = int(input("Number of rows\n"))
m = int(input("Number of columns\n"))

a = [[0] * m for i in range(n)]
b = [[0] * m for i in range(n)]
c = [[0] * m for i in range(n)]


for i in range (n):
    for j in range (m):
        a[i][j] = float(input(f"a[{i}][{j}]="))

for i in range (n):
    for j in range (m):
        b[i][j] = float(input(f"b[{i}][{j}]="))
        
for i in range (n):
    for j in range (m):
        c[i][j] =  a[i][j] +  b[i][j]
        

print("\n c =",c)