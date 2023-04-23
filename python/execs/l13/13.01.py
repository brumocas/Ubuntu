# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 10:14:40 2022

@author: bruco
"""

##determinate if it is vowels

def vowels(letter):
    letter = letter.lower()
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' :
        return True
    else :
        return False

"""
while 1 :
    letter = input("letter =")
    if letter == "-1" :
        break
    print(vowels(letter))
"""

##determinate if it is consonant

def consonant(letter):
    if vowels(letter) == False:
        return True
    else:
        return False

"""
while 1 :
    letter = input("letter =")
    if letter == "-1" :
        break
    print(consonant(letter))
"""


sentence = str(input('Sentence : \n') )
       
l = sentence.split()

result = []
        
for i in range(len(l)):
    for j in range (len(l[i])):
        if j + 1 == len(l[i]) or j - 1  < 0:
            continue
        else:
            if consonant(l[i][j-1]) == True and vowels(l[i][j]) == True and consonant(l[i][j+1]) == True:
                result.append(l[i][j-1] + l[i][j] +l[i][j+1])    
        

print(len(result),tuple(result))
               
               
        
