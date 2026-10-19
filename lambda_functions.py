'''a=lambda name,age:print("Name is",name,"age is: ",age)
a("Neha",20)

#Write a Python program to square and cube every number in a given list of integers using Lambda
list1=[1,2,3,4,5,6]
sq=list(map(lambda x: x**2,list1))
print(sq)

cube=list(map(lambda y:y**3,list1))
print(cube)

#Write a Python program to count the even and odd numbers in a given list of integers using Lambda.
list2=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
countEven=list(filter(lambda z: z%2==0,list2))
print("total Evens:",len(countEven))

countOdds=list(filter(lambda a: a%2!=0,list2))
print("total Odds:",len(countOdds))

#Write a Python program to add two given lists using map and lambda.
list3=[1,2,3,4,5,6,7]
list4=[1,2,3,4,5,6,7]
addLists=list(map(lambda i,j:i+j,list3,list4 ))
print(addLists)

#Write a Python program to sort tuples using Lambda.
tup1 = (1120, 223, 35, 444)
list_tup1=list(tup1)
sortedList=sorted(list_tup1,key=lambda x:x)
sorted_tup1=tuple(sortedList)
print(sorted_tup1)

'''


