# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:33:28 2020

@author: mrohiths
New update
"""

subSet=[]
dataSet=[]
startIndex=0
endIndex=0
inputDataLength=int(input("Please enter the length of DataSet to geenrate: "))
fold=int(input("Please enter number of elements one fold can hold: "))

dataSet=[i for i in range(inputDataLength)]
print(dataSet)

print("")


for i in range(0,inputDataLength,fold):
    if i!=0:
        endIndex=i+fold
        if endIndex >= inputDataLength:
            endIndex=inputDataLength
        startIndex=i
        print(f'start index is {startIndex} and end Index is {endIndex}')
        subSet.append(dataSet[startIndex:endIndex])
        
    else:
        endIndex=fold
        print(f'start index is {startIndex} and end Index is {endIndex}')
        print(dataSet[startIndex:endIndex])
        subSet.append(dataSet[startIndex:endIndex])

print(subSet)
