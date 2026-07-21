"""
Topic: List Methods
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of List Methods in Python.
"""

#Append
list = [1,2,3,4,5]

list.append(6) # Append add the element of the last of list
print(list) #o/p: [1,2,3,4,5,6]

list.append(7)
print(list) #o/p: [1,2,3,4,5,6,7]

#Sort
list = [88,72,45,0,3,14,788,1,65,]

list.sort() #Sort list by ascending order
print(list) #o/p: [0, 1, 3, 14, 45, 65, 72, 88, 788]

list.sort(reverse=True)
print(list) #o/p: [788, 88, 72, 65, 45, 14, 3, 1, 0]

list = ["Banana","Litchi","Apple"]
list.sort() #Sort method sort the string also
print(list) #o/p: ['Apple', 'Banana', 'Litchi']

list.sort(reverse=True)
print(list) #o/p: ['Litchi', 'Banana', 'Apple']

#Reverse
list = [88,72,45,0,3,14,788,1,65]

list.reverse() #reverse the list 
print(list) #o/p: [65, 1, 788, 14, 3, 0, 45, 72, 88]

#Insert 
# list = [Index , Element]
list = [88,72,45,0,3,14,788,1,65]

list.insert(0,786)
print(list) #o/p: [786, 88, 72, 45, 0, 3, 14, 788, 1, 65]

list.insert(1,99)
print(list) #o/p: [786, 99, 88, 72, 45, 0, 3, 14, 788, 1, 65]

#Remove 
list = [88,72,45,0,3,14,788,1,65]

list.remove(0) #Remove the element from the list 
print(list) #o/p: [88, 72, 45, 3, 14, 788, 1, 65]

list.remove(88)
print(list) #o/p: [72, 45, 3, 14, 788, 1, 65]

#POP
list = [88,72,45,0,3,14,788,1,65]

list.pop(0) #Removing the elemets using index
print(list) #o/p: [72,45,0,3,14,788,1,65]

list.pop(4)
print(list) #o/p: [72,45,0,3,788,1,65]

