#slicing index in string--
# str = "Siddik_Gadkari"
# print(str[1:4]) #o/p = idd
# print(str[7:14]) #o/p = Gadkari
# print(str[0:len(str)]) #o/p = Siddik_Gadkari

#Negative Indexing Slicing--
# str = "Apple_Mango"
# print(str[-11:-6]) #o/p = Apple 

#String Functions--
# str = "i am a coder."
# print(str.endswith("er")) #o/p = flase
# print(str.capitalize()) #o/p = I am a coder.
# print(str.replace("a","G")) #o/p = i Gm G coder.

# num = int(input("Enter a Number: "))
# if(num % 2 ==0):
#     print(num,"is even")
# else:
#     print(num,"is Odd")

# n1 = int(input("Enter 1st no: "))
# n2 = int(input("Enter 2st no: "))
# n3 = int(input("Enter 3st no: "))

# if(n1 > n2 and n1>n3):
#     print(n1,"is lagers")
# elif(n2 > n1 and n2>n3):
#     print(n2,"is lager")
# else:
#     print(n3,"is lager")

# n = int(input("Enter a no: "))
# if(n % 7 == 0):
#     print(n,"is multiple of 7")
# else:
#     print(n,"is not multiple of 7")

# movies = [] 

# m1 = input("enter fev movie: ")
# m2 = input("enter fev movie: ")
# m3 = input("enter fev movie: ")

# movies.append(m1)
# movies.append(m2)
# movies.append(m3)

# print("Your Fev Movies are: ",movies)

# list = [1,2,3,4,3,2,1]

# copy  = list.copy()
# copy.reverse()
# print("OG List:",list)
# if (copy == list):
#     print("it is a Palindrome",copy)
# else:
#     print("it is not palindrome!",copy)

# tuple = ("C","D","A","A","B","B","A")
# print(tuple.count("A"))

# dic = {
#     "table" : ["A piece of furniture","List of facts and figures"],
#     "Cat" : "A small animal"
# }
# print(dic)

# subject = {"Python","Java","C++","Python","JavaScript","Java","Python","Java","C++","C"}
# print(subject)
# print("Total Class Rooms:",len(subject))

# info = {}

# s = input("Enter Subject Name: ")
# m = int(input("Enter Subject Marks: "))
# info.update({s:m})

# s = input("Enter Subject Name: ")
# m = int(input("Enter Subject Marks: "))
# info.update({s:m})

# s = input("Enter Subject Name: ")
# m = int(input("Enter Subject Marks: "))
# info.update({s:m})
# print(info)

# set = {9, 9.0}
# print(set)