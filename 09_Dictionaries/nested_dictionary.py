"""
Topic: Nested Dictionary
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Nested Dictionary in Python.
"""
Student = {
    "Name" : "Rahul Kumar",
    "Subject" : {
        "Maths" : 74,
        "Python" : 98,
        "DSA" : 65
    },
    "CGPA" : 7.8
}

print(Student) #o/p: {'Name': 'Rahul Kumar', 'Subject': {'Maths': 74, 'Python': 98, 'DSA': 65}, 'CGPA': 7.8}
print(Student["Subject"]["Python"]) #o/p: 98
print(Student["Subject"]["Maths"]) #o/p: 74