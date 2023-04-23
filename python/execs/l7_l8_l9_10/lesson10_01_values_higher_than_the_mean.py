"""
Created on 2022

@author: António Brito / Carlos Bragança

objective:
  Calculate the arithmetic mean of a list of N values and print all the values
  that are higher than the mean
  
Variables:
  n                             -> Number of list values
  list_values                   -> list values
  list_sum                      -> sum of list values
  mean                          -> mean of list values
"""
#%%
n = int(input('Number of values = '))
list_values=[None] * n
list_sum = 0
for i in range(n):
    list_values[i] = float(input(f'Values[{i}]='))
    list_sum = list_sum + list_values[i]
mean  = list_sum / n
print ("The mean is :",mean )
for i in range(n):
    if list_values[i] > mean :        # If the value is greater than the mean
        print(f"list_values[{i}]=" , list_values[i])
