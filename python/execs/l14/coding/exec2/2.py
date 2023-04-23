# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:18:38 2022

@author: bruco
"""

def read(file):
    fh = open(file,"r")
    
    l = []
    
    sentence = fh.readline()

    while sentence != "" :
        l.append(sentence.strip())
        sentence = fh.readline()
    fh.close()
    
    return l



file1 = str(input("Filename 1:"))
file2 = str(input("Filename 2:"))

names =read(file1)
surname =read(file2)

for i in range(len(names)) :
    for j in range(len(surname)) :
        print(f"{names[i]} {surname[j]}")
        