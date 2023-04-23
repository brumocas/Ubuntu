# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 15:07:24 2022

@author: bruco
"""

n = [1,2,5,4,2,6,3,7,7,3,21]

add = 0.0
mean = 0.0

for i in n :
    add = add + i

mean = float(add) / len(n)
print(f"Mean = {mean}")

for i in n :
    if i > mean :
        print(i)
    

