# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 09:31:21 2022

@author: bruco
"""
import math 
import sys

print("Quadratic root solver type:\n (ax^2 + 2abx + b^2) = 0")

a = int(input("a ="))
b = int(input("b ="))
c = int(input("c ="))

delta = b**2 - (4 * a * c)

if delta < 0 :
    print("\nNo real roots")
    sys.exit()

if delta == 0:
    print("\n2xRoot : \nx =",-b/(2 * a))
else:
    x1 = ((- b + math.sqrt(delta)) / (2*a))
    x2 = ((-b - math.sqrt(delta))/ (2*a))
    print(f"\nRoots \nx1 = {x1:.2f}")   
    print(f"x2 = {x2:.2f}")   