# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 19:19:05 2022

@author: bruco
"""

n = int(input("Number of elements\n"))
a = [0]*n
b = [0]*n

for i in range(n):
    a[i] = float(input("a["+str(i)+"]="))
                 
for i in range(n):
    b[i] = float(input("b["+str(i)+"]="))

scalarprod = 0.0

for i in range(n):
    scalarprod = scalarprod + a[i]*b[i]
          

print("Scalar product =",scalarprod)