#!/usr/bin/env python
# coding: utf-8

# Create a new function called listDivide that takes in two parameters, a list called numbers 
# and an integer called divide that defaults to 2
def listDivide(numbers, divide = 2):
    counter = 0
    for number in numbers:
        if(number % divide == 0):
            counter = counter + 1
    return counter

# Create a custom exception class called ListDivideException 
class ListDivideException(Exception):
    pass

# Create another function called testListDivide that performs various tests on ListDivide
def testListDivide():
    print (listDivide([1,2,3,4,5]) == 2)
    print (listDivide([2,4,6,8,10]) == 5)
    print ((listDivide([30, 54, 63,98, 100], divide=10) == 2))
    print (listDivide([]) == 0)
    print (listDivide([1,2,3,4,5], 1) == 5)

testListDivide()
