# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:37:43 2022

@author: bruco
"""

n = int(input())
m = int(input())
p = int(input())

a = [[0] * m for i in range(n)]
b = [[0] * p for i in range(m)]
c = [[0] * p for i in range(n)]



for i in range (n):
    for j in range(m):
        a[i][j]= float(input())
        
for i in range (m):
    for j in range(p):
        b[i][j]= float(input())
        
for i in range(n): ##iterate through rows of a 
    for j in range(p):  ##iterate through columns  of b 
        for k in range(m): ##iterate through rows of b 
            c[i][j] += a[i][k]*b[k][j]

for i in range(n):
    print(c[i])