# -*- coding: utf-8 -*-
"""
Created on Mon May 11 19:52:53 2020

@author: mrohiths
Lambda function: 
    Most of the use cases of Lambda functions can be replaced by using list 
    comprehensions. 
    Lambda functions do not create function names in local namespace. 
    the structure is as follows
    lambda -space-  arguments seperated with coma: expression to evaluate
    for eg: lamda x: x %2 == 0 
    lambda returns a function object. 
    
    
Filter object returns a filter object. 
    Filter takes an iterable and a function as arguments, it applies the function
    on the iterable and returns only those that return true. 

Map function: 
    Applies a function to all elements in an iterable. 

reduce Function: 
    
    

"""

list1 = [ 1 , 2 , 3 , 4 , 5 , 6 ]
list1 = list(filter( lambda x: (x % 2 == 0 ) , list1))
print(list1)