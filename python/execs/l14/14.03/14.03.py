# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 12:22:29 2022

@author: bruco
"""

def write(file,numbers):

    fh = open(file,"w")

    for i in range(len(numbers)):   
        fh.write(f"{numbers[i]}\n")
    
    fh.close()

    return 0
"-----------------------------------------------------------------------------"
"""
função que le um ficheiro e devolve uma lista com os numeros
param:
    file = ficheiro onde ler
    numbers = lista com os numeros lidos
"""

def read(file):
    fh = open(file,"r")
    line = fh.readline()
    numbers = []

    while line != "" :
        f = line.strip().split(',')
        numbers.append(f[0])
        line = fh.readline()
        
    print(numbers)
    fh.close()

    return numbers

"-----------------------------------------------------------------------------"


numbers1 = read("file1.csv")
numbers2 = read("file2.csv")
numbers3 = []

n1 = len(numbers1)
n2 = len(numbers2)

dif = abs (n2 - n1)

print("dif =",dif)

if n2 > n1 :
    for i in range (n1):
        average = float((int(numbers1[i]) + int(numbers2[i]))/2)
        numbers3.append(average)
    for i in range(n1,n2) :
        numbers3.append(int(numbers2[i])/2)         
else :
    for i in range (n2):
        average = float((int(numbers1[i]) + int(numbers2[i]))/2)
        numbers3.append(average)
    for i in range(n2,n1) :
        numbers3.append(int(numbers1[i])/2)

write("file.csv",numbers3)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        