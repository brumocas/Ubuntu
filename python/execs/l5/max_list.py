# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:30:09 2022

@author: bruco
"""


n = int(input())

i = 1
number = int(input())
high = number
pos = 1

while i < n:
    number = int(input())
    if number > high :
        high = number 
        pos = i + 1
    i = i +1
        
print("Maximum =",high,"position =",pos)