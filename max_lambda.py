# -*- coding: utf-8 -*-
"""
Created on Sun May 17 10:53:48 2020

@author: mrohiths

max takes n arguments and print the maximum  of the arguments. 
You can give default= and key= 
Key will a function that can be appleid to the list of arguments, based on the 
result the arguments will be sorted. 

"""

lst = [2, 4, 5, 7, 8, 25]
max_divisble_by_five = max(lst, key=lambda x: x / 5 )
print(max_divisble_by_five)
divisble_by_5 = lambda x: x / 5
max_divisble_by_five = max(lst, key=divisble_by_5)
print(max_divisble_by_five)




