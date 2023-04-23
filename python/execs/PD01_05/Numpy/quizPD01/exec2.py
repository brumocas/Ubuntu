# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:52:10 2022

@author: bruco
"""

import numpy as np 

r = int(input("Number of rows ="))

c = int(input("Number of columns ="))

a = []


for i in range (r):
    for k in range (c):
        a.append(int(input(f"a[{i},{k}]=")))
        
npa = np.array(a)
res = npa.reshape(r,c)

det = np.linalg.det(res)

print(f"Determinant = {det:.1f}")

inv = np.linalg.inv(res)

print("Matrix inverse:")

for i in range (len(inv)):
    print(inv[i])