"""
Topic: List Indexing
Author: Siddik Imran Gadkari
Date: 20 July 2026

Description:
This program demonstrates the use of List Indexing in Python.
"""
#indexing of list 
marks = ["Siddik",88,"Samarth",92,"Shubham",70,"Aditya","Shreyash",17] #indexing start with 0 
# print(marks[0]) #o/p:88
# print(marks[5])#o/p:75
# print(marks[7])#o/p:56

#update list with indexing
print(marks[3],"Before Updating") #o/p:Samarth
marks[3]="Jack"  #change value using indexing 
print(marks[3],"After Updating") #o/p:Jack

