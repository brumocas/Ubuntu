# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:13:40 2022

@author: bruco
"""
def frequency_grades(l):
    freq = [0]*21
    for i in range(1,21):
        for j in range(len(l)):
            if l[j] == i :
                freq[i] += 1
    
    for i in range(6,21):
        print(f"{i} ==",float(freq[i]/len(l))*100,"%")
  
    return 0

n = int(input("Number of students :"))

l = []

for i in range(n):
    l.append(int(input()))
    
frequency_grades(l)

