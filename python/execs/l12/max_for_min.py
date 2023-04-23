# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:57:23 2022

@author: bruco
"""
n = int(input())


a = [[0] * n for i in range(n)]

for i in range (n):
    for j in range(n):
        a[i][j]= float(input())

m1 = 0
m2 = 0

m = a[0][0]
for i in range (n):
    for j in range(n):
        if a[i][j] < m :
            m = a[i][j]
            m1 = i
            m2 = j

M1 = 0
M2 = 0            
M = a[0][0]
for i in range (n):
    for j in range(n):
        if a[i][j] > M:
            M = a[i][j]
            M1 = i
            M2 = j

a[m1][m2] = M
a[M1][M2] = m
        
        
for i in range(n):
    print(a[i])
        