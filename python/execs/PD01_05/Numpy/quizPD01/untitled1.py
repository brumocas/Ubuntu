# -*- coding: utf-8 -*-
"""
Created on Mon May  2 17:37:16 2022

@author: bruco
"""

import numpy as np 

n = int(input("Number of elements:"))

a = []
b = []

for i in range (n):
    a.append(int(input(f"a[{i}]:")))

for i in range (n):
    b.append(int(input(f"b[{i}]:")))
    

c = sum(np.array(a) * np.array(b))

print(f"Scalar product = {c:.1f}")