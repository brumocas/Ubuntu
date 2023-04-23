# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:30:51 2022

@author: bruco
"""

"""
fh = open('test.txt','w')

for i in range(5) :
    fh.write(f'line{i}\n')

fh.close()
"""

"""
fh = open('test.txt','r')

lines = fh.read()

print(lines)

fh.close()
"""

"""
fh = open("test.txt","r")

line = fh.readline().strip()

while line != "":
    print(line)
    line = fh.readline().strip()

fh.close()
"""

fh = open("test.txt","r")

lines = list(map(str.strip,fh.readlines()))

print(lines)

fh.close()





















