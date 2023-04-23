# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 18:04:24 2022

@author: bruco
"""
num = int(input())
factorial = 1


while num != 1:
       factorial = factorial*num
       num = num - 1
       
print("Factorial =",factorial)