# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 14:24:52 2022

@author: bruco
"""

def read(file):
    fh = open(file,"r")
    
    sentence = list(map(str.strip,fh.readlines()))
    
    return sentence


file = str(input("Filename:"))

name_id = str(input("Name id:"))

l = read(file)

for i in range (len(l)):
    if l[i].find(name_id) != -1:
        print(l[i])
                              
        




    
