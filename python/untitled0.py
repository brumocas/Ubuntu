# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:45:46 2022

@author: bruco
"""

import math 
pi = math.pi

def time_until_lost_connection(direction_A,direction_B):
    r = 35/math.sqrt(2)  
    pos_a = r*math.cos(math.radians(direction_A)) + r*math.sin(math.radians(direction_A))
    pos_b = r*math.cos(math.radians(direction_B),math.radians(direction_B)) 
    
    
    return round(result,3)

print(time_until_lost_connection(10,10))