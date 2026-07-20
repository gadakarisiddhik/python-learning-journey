"""
Topic: If Elif Else
Author: Siddik Imran Gadkari
Date: 20 July 2026

Description:
This program demonstrates the use of Conditional Statement in Python.
"""
#if Statement 
age = 18
if(age >= 18): #check condition and take decision
    print("Your can vote")

#if-elif-esle
light = "green"
if (light=="red"):
    print("Stop")
elif(light=="green"): #elif check ondition whenever if condition is false
    print("Go")
elif(light=="yellow"):
    print("Look")
else:                 #else alwayes run whenever if and elif condtions are false
    print("Wrong Input")