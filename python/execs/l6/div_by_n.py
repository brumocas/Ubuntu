# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 13:53:09 2022

@author: bruco
"""

n = int(input())

print(f"Factors of {n}")

for i in range(1,n+1):
    if n % i == 0:
        print(i)