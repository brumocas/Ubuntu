# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 13:42:25 2022

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

l1 =read(file1)
l2 =read(file2)

l1 = l1 + l2

for i in l1:
    print(i)