"""
Topic: While Loop
Author: Siddik Imran Gadkari
Date: 21 July 2026

Description:
This program demonstrates the use of While Loop in Python.
"""
#Print 10 Times Hello Using While Loop
count = 1
while count <= 10 : #while Condition
    print("Hello") #o/p: "Hello*10
    count += 1
print(count) #o/p: 11

#Print 2's Table Using While Loop
i=1
n = int(input("Enter a number for table: "))
while i <= 10 :
    print("2 *",i,"=",n*i) 
    i += 1

#Reverse While loop
count = 10
while 1 <= count:
    print("2 *",count,"=",2*count)
    count -= 1

i = 1
while i <= 100 :
    print(i)
    i+=1 

i = 100 
while i >= 1:
    print(i)
    i-=1

list = [10,24,64,58,94,65,86,565,56]
i = 0
while i <= len(list)-1 : 
    print(list[i])
    i+=1

tuple = (12,2665,4,0,115,66,78,98,44)
key = int(input("Enter your no: "))
i = 0
while i <= len(tuple)-1:

    if(tuple[i] == key):
        print(tuple[i],"no founded at",i,"Position")
    else:
        print(key,"not found at",i,"Postion!")
    i += 1
