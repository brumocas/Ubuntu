# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 15:10:20 2022

@author: bruco
"""

def words_start_vowel(string):
    l = []
    l = string.split()
    start = 0
    
    for i in range (len(l)):
       
        aux = l[i][0]
        aux = aux.lower()
        if aux == 'a' or aux == 'e' or aux == 'i' or aux == 'o' or aux == 'u':
            start = start + 1
    
    return start
