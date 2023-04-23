# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:59:24 2022

@author: bruco
"""

fh = open("test.txt","r")

s = 0

count = 0

line = fh.readline().strip()

l = line.split()

while line != "":
    for i in range(len(l)):
        s += int(l[i])
        count += 1
        print(int(l[i]))
    line = fh.readline().strip()
    l = line.split()

print(f"File mean ={float(s/count):.2f}")
    
fh.close()