"""
Topic: Nested Dictionary
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of Nested Dictionary in Python.
"""

#dictionary Created 
info = {
    "Name" : "Siddik",
    "Subject" : ["Python","Java","SQL"],
    "Project" : ("Chatbot","Calculator","Gym Management"),
    "Age" : 20,
    "Adult" : True,
    "CGPA" : 7.5
}

#Keys 
print(info.keys()) #o/p: dict_keys(['Name', 'Subject', 'Project', 'Age', 'Adult', 'CGPA'])

#Values 
print(info.values()) #o/p: dict_values(['Siddik', ['Python', 'Java', 'SQL'], ('Chatbot', 'Calculator', 'Gym Management'), 20, True, 7.5])

#Items
print(info.items()) #o/p: return key and values , dict_items([('Name', 'Siddik'), ('Subject', ['Python', 'Java', 'SQL']), ('Project', ('Chatbot', 'Calculator', 'Gym Management')), ('Age', 20), ('Adult', True), ('CGPA', 7.5)])

#Get
print(info.get("Name")) #o/p: Siddik
print(info.get("Subject")) #o/p: ['Python', 'Java', 'SQL']
print(info.get("Adult")) #o/p: True

#Update 
info.update({"City" : "Kolhapur"})
print(info) #o/p: {'City': 'Kolhapur'}

info.update({"PinCode" : 416122})
print(info) #o/p: {"PinCode" : 416122}