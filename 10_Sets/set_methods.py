"""
Topic: Set Methods
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Set Methods in Python.
"""

#Add
collection = {1,"Siddik",2,"Samarth",3,"Shubham"}
collection.add(786) #add an element
print(collection) #o/p: {1, 2, 3, 786, 'Siddik', 'Samarth', 'Shubham'}

#Remove
collection = {1,"Siddik",2,"Samarth",3,"Shubham"}
collection.remove("Samarth") #remove an element
print(collection) # o/p: {1, 2, 3, 'Shubham', 'Siddik'}

#clear 
collection = {1,"Siddik",2,"Samarth",3,"Shubham"}
collection.clear() #Empties the set
print(collection) #o/p: set()

#POP
collection = {1,"Siddik",2,"Samarth",3,"Shubham"}
collection.pop() #Remove a random Value
print(collection) #o/p: {1, 2, 3, 'Shubham', 'Siddik'}

#Union
collection = {1,2,3}
collection1 = {3,4,5}
print(collection.union(collection1)) #o/p: {1, 2, 3, 4, 5} , Combines the both sets values and return new

#Intersection
collection = {1,2,3}
collection1 = {3,4,5}
print(collection.intersection(collection1)) #o/p: {3} , Combines comman values and return new

collection = {1,2,3}
collection1 = {3,2,5}
print(collection.intersection(collection1)) #o/p: {2,3}