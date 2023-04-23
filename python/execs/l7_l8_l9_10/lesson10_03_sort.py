"""
Created on 2022

@author: António Brito / Carlos Bragança

objective:
  Sort a list of N elements in ascending order.
  
Variables:
    n - number of values
    list_values - List of values    

"""
#%% Version 1
n = int(input("Enter the number of elements in the list ="))
list_values=[None]*n

for k in range(n):        # Loop to read the list values
    list_values[k] = int(input(f"list_values[{k}]="))

for i in range(n-1):  
    K = i + 1
    for k in range(i+1, n):
        if list_values[i] > list_values[k]:
            temp = list_values[i]
            list_values[i] = list_values[k]
            list_values[k] = temp

print("The sorted vector is: ")
for k in range(n):
    print(list_values[k])
#%% Version 2
n = int(input("Enter the number of elements in the list ="))
list_values=[None]*n

for k in range(n):        # Loop to read the list values
    list_values[k] = int(input(f"list_values[{k}]="))

list_values.sort()

print("The sorted vector is: ")
for k in range(n):
    print(list_values[k])
