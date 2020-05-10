# -*- coding: utf-8 -*-

"""
  Input a list of numbers. 
  1.) Replace all integers divisble by 3 into fizz
  2.) Replace all integers divisible by 5 into buzz.
  3.) Replace all intergers divisible by 3 and 5 to fizzbuzz. 

"""

numbers = [ 3, 5, 15, 45, 75, 2, 10]

for i, j in enumerate(numbers):
    if j % 5 == 0 and j % 3 == 0:
        numbers[i] = "fizzbuzz"
    elif j % 3 == 0:
        numbers[i] = "fizz"
    elif j % 5 == 0:
        numbers[i] = "buzz"
    else:
        pass
    
print(numbers)