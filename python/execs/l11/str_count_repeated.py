# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:30:34 2022

@author: bruco
"""

sentence = str(input("Sentence :\n"))

l =[]

l = sentence.split()

unique = set(l)

words = list(unique)

count = []

for i in words:
    aux = l.count(i)
    count.append(aux)
    
print("Frequency of the words :\n")

for i in range(0,len(words),1):
    print(f"{words[i]}= {count[i]}")
    
    