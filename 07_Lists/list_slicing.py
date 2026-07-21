"""
Topic: List Slicing
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of List Slicing in Python.
"""

#List Slicing 
#list[starting_index : Ending_Index] Ending Index is not included

marks = [55,88,77,99,105]
print(marks[1:3]) #o/p: [88,77]
print(marks[0:len(marks)]) #o/p: [55, 88, 77, 99, 105]

#List Negative Indexing

marks = [55,88,77,99,105]
print(marks[-5 : -2]) #o/p: [55,88,77]
print(marks[-5 : -1]) #o/p: [55,88,77,99]