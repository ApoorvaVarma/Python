'''#Exercise 1: Basic Dictionary Operations
person ={'name': 'Alice','age':25}
print(person['name']) 
print(person['age'])
 
person["Company"]="Microsoft"
print(person["Company"])

del[person['age']]
print(person)


#Exercise 2: Dictionary Operations
person ={'name': 'Alice','age':25}
person["Company"]="Microsoft"
print(person)

del[person['age']]
print(person)

#Exercise 3: Dictionary from Two Lists
a=["Name","Emp_id","Company"]
b=["Apoorva",14563,"XYZ technologies"]

new_dict=dict(zip(a,b))
print(new_dict)
#Exercise 4: Clear Dictionary
person ={'name': 'Alice','age':25}
person.clear()
print(person)

#Exercise 5: Merge Dictionaries
person1 ={'name': 'Alice','age':25}
person2 ={'subject': 'English','Class':"MBA"}
print(person1|person2)


#another method
person1 ={'name': 'Alice','age':25}
person2 ={'subject': 'English','Class':"MBA"}
a={**person1,**person2}
print(a)

#Exercise 6: Access Nested Dictionary

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}
student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print(person["address"]["zip"])
#Exercise 7: Access ‘history’ Key From a Nested Dictionary

student = {"name": "Dave", "grades": {"math": 88, "science": 92, "history": 75}}
print(student["grades"]["history"])


#Exercise 8: Initialize Dictionary with Default Values
a=['name','age','subject']
b=25
c=dict.fromkeys(a,b)
print(c)


#Exercise 9: Rename a Key of Dictionary
student = {"name": "Dave", "grades": 'a','city':"Delhi"}
student["First_name"]="Dave"
print(student)
student.pop("name")
print(student)
#another way
student = {"name": "Dave", "grades": 'a','city':"Delhi"}
student["firstname"]=student.pop("name")
print(student)
'''

#Exercise 10: Delete a List of Keys
student = {"name": "Dave", "grades": 'a','city':"Delhi","subject":"English","University":"IIT"}
list1=["subject","University"]
for i in list1:
    student.pop(i)
print(student)