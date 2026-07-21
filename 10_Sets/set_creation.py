"""
Topic: Set Creation
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Set Creation in Python.
"""
"""
Set is collection of unordered items,
Each elements in the set must be unique and immutable.
"""
#Set Cteation
collection = {1,2,3,4}

print(type(collection)) #o/p: <class 'set'>
print(collection) #o/p: {1,2,3,4}

#String,int,flaot 
collection = {1,"Siddik",2,"Samarth",3,"Shubham"}

print(type(collection)) #o/p: <class 'set'>
print(collection) #o/p: {1, 2, 3, 'Siddik', 'Samarth', 'Shubham'}

#Similer Values in list
collection = {1,"Siddik",2,"Samarth",3,"Shubham",1,"Siddik"}

print(type(collection)) #o/p: <class 'set'>
print(collection) #o/p: {1, 2, 3, 'Siddik', 'Samarth', 'Shubham'}, ignore similer values

#creating Empty Set
set = set() 
print(set) #o/p: set()
