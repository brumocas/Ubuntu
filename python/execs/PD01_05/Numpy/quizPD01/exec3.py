# -*- coding: utf-8 -*-
"""
Created on Mon May  2 18:12:06 2022

@author: bruco
"""

import numpy as np 

l = []

a = []

l.append(str(input()))

a.append(l[0].split(','))

n = len(a[0])

for i in range (n):
    l.append(str(input()))

for i in range (1,n):
    a.append(l[i].split(','))

b = l[n].split(',')

for i in range (n):
    for k in range(n):
        a[i][k] = int(a[i][k])

for i in range(n):
    b[i] = int(b[i])
    
result = np.linalg.solve(np.array(a),np.array(b))

print("solution:\n",result)