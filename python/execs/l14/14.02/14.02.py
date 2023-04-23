# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 11:43:20 2022

@author: bruco
"""
"""
função que escreve num ficheiro uma lista com numeros
param:
    file = ficheiro onde escrever
    numbers = lista com os numeros a escrever
"""
def write(file,numbers):

    fh = open(file,"w")

    for i in range(len(numbers)):   
        fh.write(f"{numbers[i]}\n")
    
    fh.close()

    return 0

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



numbers1 = read("file1.csv")
numbers2 = read("file2.csv")

for i in range(len(numbers2)):
    numbers1.append(numbers2[i])

write("file3.csv",numbers1)