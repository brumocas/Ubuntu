# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 09:59:21 2022

@author: bruco
"""


n1 = int(input("Number of elements in first list = "))

l1 = []

for i in range(n1):
    l1.append(int(input(f"l1[{i}]=")))


n2 = int(input("Number of elements of second list = "))

l2 = []

for i in range(n2):
    l2.append(int(input(f"l2[{i}]=")))
    
    
setl1 = set(l1)
setl2 = set (l2)

comon = setl1.intersection(setl2)

result = list(comon)

result.sort()

print(result)

