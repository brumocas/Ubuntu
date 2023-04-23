# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 10:16:19 2022

@author: bruco
"""

number = [1,2,4,2,342,3,1,26,2]

max_1 = max_2 = int(number[0])


for i in range(len(number)) :
    if max_1 < int(number[i]):
        max_1 = int(number[i]);
        
for i in range(len(number)) :
    if max_2 < int(number[i]) and int(number[i]) != max_1 :
        max_2 = int(number[i]);

print(max_1)
print(max_2)