# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:44:44 2022

@author: bruno costa
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





numbers1 = [5,100]
numbers2 = [30,10,7]

write("file1.csv",numbers1)
write("file2.csv",numbers2)

read("file1.csv")
read("file2.csv")






