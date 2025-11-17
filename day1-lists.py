#----------------------------Lists---------------------------------#
#!Printing a list of students using for loop

# students = ["Alex","Ron","Hermione","Harry"]
# for student in students:
#     if student == "Ron":
#         continue
#     print(student)
    
#!Use of Len() function 
# students = ["Alex","Ron","Hermione","Harry"]
# for i in range(len(students)):
#     print(i,students[i])
    
#!Use of dictionary

# ?Stores data in key–value pairs
# ?Very fast lookups
#? Written in {key: value}
#* Example:
# person = {"name": "Sangam", "age": 20}
# print(person["name"])  # Sangam

# capitals = {"USA": "Washington", "China": "Beiging", "Nepal": "Kathmandu","UAE":"Dubai"}

#capitals.update({"USA":"Newyork"})
#capitals.pop("China")#this removes china
#capitals.popitem() #removes the last key value pair
#capitals.clear() #removes every elem
#keys = capitals.keys()# gives every key
#values = capitals.values()# gives every value
#items=capitals.items() #prints every key value pair in the form of tuples
#print(items) #[('USA', 'Washington'), ('China', 'Beiging'), ('Nepal', 'Kathmandu'), ('UAE', 'Dubai')]

'''
students = {
    "Harry":"Gryffindor",
    "Hermione":"Gryffindor",
    "Ron":"Gryffindor",
    "Malfoy":"Slytherin"
}


for student in students:
    print(student,students[student] , sep=',')
    
'''
students= [
    {"name":"Hermione","house":"Gryffindor","patronus":"Otter"},
    
    {"name":"Harry","house":"Gryffindor","patronus":"Stag"},
    
    {"name":"Ron","house":"Gryffindor","patronus":"Jack Russel"},
    
    {"name":"Draco","house":"Slytherin","patronus":"None"}
]

for student in students:
    print(student["name"],student["house"],sep="-> ")