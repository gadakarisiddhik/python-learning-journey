"""
Topic: Dictionary Creation
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Dictionary Creation in Python.
"""
"""
Dictionry  are used for store data values in key values pair,
they are unordered, mutable(Changeble) and don't allow duplicates
"""

info = {
    "key" : "Value",
    "Name" : "Siddhik",
    "Learning" : "Python"
} #this is a creation of a dictionary key and values

print(type(info)) #o/p: <class 'dict'>
print(info) #o/p: {'key': 'Value', 'Name': 'Siddhik', 'Learning': 'Python'}

demo = {
    "Name" : "Siddhik",
    "Roll" : "163",
    "Div" : "A"
}

print(type(demo)) #o/p: <class 'dict'>
print(demo) #o/p: {'Name': 'Siddhik', 'Roll': '163', 'Div': 'A'}

#Empty Dictionary or Null Dictionary
info = {}
print(info) #o/p: {}

#Dictionary creation With List & Tuple
info = {
    "Name" : "Siddik",
    "Subject" : ["Python","Java","SQL"],
    "Project" : ("Chatbot","Calculator","Gym Management"),
    "Age" : 20,
    "Adult" : True,
    "CGPA" : 7.5
}

print(type(info)) #o/p: <class 'dict'>
print(info) #o/p: {'Name': 'Siddik', 'Subject': ['Python', 'Java', 'SQL'], 'Project': ('Chatbot', 'Calculator', 'Gym Management'), 'age': 20, 'Adult': True, 'CGPA': 7.5}

#values access by key
print(info["Name"]) #o/p: Siddik
print(info["Adult"]) #o/p: True
print(info["Age"]) #o/p: 20
print(info["CGPA"]) #o/p: 7.5
print(info["Subject"]) #o/p: ['Python', 'Java', 'SQL']
print(info["Project"]) #o/p: ('Chatbot', 'Calculator', 'Gym Management')

#updating and adding Values using Key
info = {
    "Name" : "Siddik",
    "Subject" : ["Python","Java","SQL"],
    "Project" : ("Chatbot","Calculator","Gym Management"),
    "Age" : 20,
    "Adult" : True,
    "CGPA" : 7.5
}

info["Name"] = "Samarth"
print(info) #o/p: {'Name': 'Samarth',}

info["CGPA"] = 9.50
print(info) #o/p: {'CGPA': 9.50,}

info["Adult"] = False
print(info) #o/p: {'Adult': False,}

info["Surname"] = "Stark"
print(info) #o/p: added new key and value of the end {'Surname': "Stark",}

info["Attendence"] = 78
print(info) #o/p: added new key and value of the end {'Attendence': 78,}

info["Grade"] = "A2"
print(info) #o/p: added new key and value of the end {'Greade': "A2",}