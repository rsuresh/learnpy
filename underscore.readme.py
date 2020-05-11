# -*- coding: utf-8 -*-
"""
Created on Mon May 11 20:52:02 2020

@author: mrohiths

Underscores : 
    _ 
        are used as throwaway variables and function names.
        
    Variable or methods starting with Single Underscore 
        _ prefixed to a variable or a method is used to hint that the function is a 
        private variable/method. This is just an agreed upon convention to inform the coder. 
        You may access the variables from outside, and it will be still acessible. 

    Variable_ Variable prefixed with underscore. 
        If variable name is already used as a keyword in Python then we can use this. 
        by convention. 
        For eg: use class_ if we use a variable named class. If we need to use a variable
        named def use def_ . Avoid as much as possible. 
    
    __var , Variable prefixed with two underscores. 
        A variable prefixed with two underscores will be renamed by Python itnerpretor. 
        The process is called name mangling. This is done avoid collisions when you 
        extend a class.  CHeck more on Name managling in  
        https://dbader.org/blog/meaning-of-underscores-in-python 
        
     __method__, Prefixed and suffixed by underscores. 
         This is to signy that method is a dunder method.  This should only be used for
         dunder methods
         
     
        
    
"""

