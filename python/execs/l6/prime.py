# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:29:36 2022

@author: bruco
"""
n = int(input())

count_div = 0

for i in range(1,8):
    if n % i == 0 and i < n:
        count_div = count_div + 1
    
if count_div < 2:
    print(f"{n} is prime")
    
else :
    print(f"{n} is not prime")