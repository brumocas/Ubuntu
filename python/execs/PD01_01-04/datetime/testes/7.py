# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 00:23:55 2022

@author: bruco
"""

import time 

sec = int(input("Number of seconds:"))

t = time.localtime(sec)

result = time.strftime("%a %b %d %H:%M:%S %Y",t)

print(result)