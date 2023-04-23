# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 14:22:18 2022

@author: bruco
"""

sentence = str(input("Sentence :\n"))

vowels = 0

for i in sentence :
    i = i.lower()
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        vowels = vowels + 1; 
        
print(f"Vowels = {vowels}")