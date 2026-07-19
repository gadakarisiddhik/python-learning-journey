"""
Topic: #o/p:pl
Author: Siddik Imran Gadkari
Date: 19 July 2026

Description:
This program demonstrates the use of String Slicing Operation in Python.
"""

#Slicing 
# str[Starting index : Ending index]

str = "Maharashrta"
slice = str[1:4]
print(slice) #print charector between  1 to 4
print(str[4:11]) #o/p:rashtra
print(str[0:len(str)]) #o/p:Maharashrta

#Slicing with Negative Index
str = "Apple"
print(str[-3:-1]) #o/p:pl
print(str[-5:-2]) #o/p:app