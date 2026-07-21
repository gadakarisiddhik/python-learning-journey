"""
Topic: Tuple Methods
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Tuple Methods in Python.
"""
#Index , Find the Element have wich position frist time 
tuple = (80,80,87,16,67,16,1,4,1)

print(tuple.index(80)) #o/p: 0 th Positon
print(tuple.index(1)) #o/p: 6 th Positon
print(tuple.index(16)) #o/p: 3 th Positon

#Count , counts total occurrence
tuple = (80,80,87,16,67,16,1,4,1)

print("Total Count:",tuple.count(80)) #o/p: 2 times
print("Total Count:",tuple.count(1)) #o/p: 2 times
print("Total Count:",tuple.count(67)) #o/p: 1 times