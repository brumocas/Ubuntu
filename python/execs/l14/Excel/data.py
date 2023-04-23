# -*- coding: utf-8 -*-
"""
Created on Mon Apr 11 10:44:44 2022

@author: bruco
"""

names = ['Bruno','Joana','Pedro']
ages = [19,23,20]
phones = [9830123,8103812,8130281]

fh = open("data.csv","w")

for i in range(len(names)):
    fh.write(f"{names[i]},{ages[i]},{phones[i]}\n")
    
fh.close()


fh = open("data.csv","r")

line = fh.readline()

names = []
ages = []
phones = []

while line != "" :
    f = line.strip().split(',')
    names.append(f[0])
    ages.append(int(f[1]))
    phones.append(int(f[2]))
    line = fh.readline()



print(names,ages,phones)
fh.close()
