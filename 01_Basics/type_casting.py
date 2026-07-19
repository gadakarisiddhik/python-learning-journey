"""
Topic: Typecast
Author: Siddik Imran Gadkari
Date: 19 July 2026

Description:
This program demonstrates the use of ypecast in Python.
"""

#type casting 

a = "2"
print(type(a)) # A is string datatype

b = 13
print(type(b)) # B is int datatype

c = int(a) # A string value typecast by int C value 
print(type(c)) #o/p: INT
print(c+b) #addition of INT and String Datatype

d = float("5.2")
print(type(d),d) # string to float

e = str(125)
print(type(e),e) #int to string