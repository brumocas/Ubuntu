# -*- coding: utf-8 -*-
"""
Created on Sat Mar 26 16:19:38 2022

@author: bruco
"""

die_faces = [1,1,2,3,1,2,1,3,4,5,2,5,6,2,1]

freq = [0]*6

for i in die_faces :
    if i == 1 :
        freq[0] += 1
    elif i == 2 :
        freq[1] += 1
    elif i == 3 :
        freq[2] += 1
    elif i == 4 :
        freq[3] += 1
    elif i == 5 :
        freq[4] += 1
    elif i == 6 :
        freq[5] += 1


for i in range(1,7):
    percentage = 100*(freq[i-1] / len(die_faces))
    print(f"Face {i} = {percentage:.2f}%")
    
