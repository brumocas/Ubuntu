# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:20:16 2022

@author: bruco
"""

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n-1)*n
        

print(fact(4))