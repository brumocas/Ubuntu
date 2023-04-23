# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 20:24:54 2022

@author: bruco
"""

n = int(input())

i = 1
count = 0

while i <= n:
    if n % i == 0:
        count = count + 1
        i = i + 1
    else :
        i = i + 1
 
if count == 2:
    print(f"{n} is prime")    
else:    
    print(f"{n} is not prime")

        