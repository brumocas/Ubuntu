"""
Created on 2022

@author: António Brito / Carlos Bragança

objective:
  When rolling a die N times determine the frequency of the numbers from 1 to 6
  
Variables:
        n  -> Number of times to roll the die
        ct -> Counter of the number of times a number came out
"""
#%% Version 1
import random
# if wanted to reproduce the same random sequence use the same seed
# random.seed(7)
n = int(input("Number of rolling :"))
ct = [0] * 7

for k in range(n):
    number = int(6 * random.random()) + 1
    ct[number] = ct[number] + 1

for k in range(1, 6 + 1):
    print(f'{k} - {ct[k]} - {100 * ct[k] / n}%')
#%% Version 2 (using dictionaries)
import random
# if wanted to reproduce the same random sequence use the same seed
# random.seed(7)
n = int(input("Number of rolling :"))
ct = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

for k in range(n):
    number = int(6 * random.random()) + 1
    ct[number] = ct[number] + 1

for k in range(1, 6 + 1):
    print(f'{k} - {ct[k]} - {100 * ct[k] / n}%')
