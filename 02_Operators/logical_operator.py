"""
Topic: Logical Operators
Author: Siddik Imran Gadkari
Date: 19 July 2026

Description:
This program demonstrates the use of Logical Operator in Python.
"""

#logical NOT
key = True
a = 50
b = 20
print("NOT Operator ",not a<b) #reverse order True ,o/p: True
print("NOT Operator ",not key) #NOT Logical Operator Revese the order , True to false , false to true ,o/p: False

#logical AND
val1 = True
Val2 = True
Val3 = False
print("AND Operator: ",val1 and Val2) #when ever both values are true then ans is true , and when ever frist value true and second value is flase then ans false ,o/p: True
print("AND Operator: ",val1 and Val3) #O/p: flase

#logical OR
a = True
b = False
c = True
d = False
print("OR Operator: ",a or b) #when ever at least one are true then ans is True ,o/p: True
print("OR Operator: ",d or c) #both values are flase then ans is false , O/p: False