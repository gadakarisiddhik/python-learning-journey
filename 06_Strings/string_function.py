"""
Topic: String Function
Author: Siddik Imran Gadkari
Date: 19 July 2026

Description:
This program demonstrates the use of String Function in Python.
"""

#endswith function
str = "i am a coder" #simple string
print(str.endswith("er")) #if string ends with parameter then gives True other wise False
print(str.endswith("am")) #O/p: False

#Captalize funtion 
str = "i am a coder"
print(str.capitalize()) #capitilize Frist Char, o/p: I am a coder

#replace Funtion , funtion(old,new)
str = "i am a coder"
print(str.replace("a","K")) #replace a from K

#count funtion 
str = "i am a coder"
print(str.count("a")) # give total count of the char in exist sting
