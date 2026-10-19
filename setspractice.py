#Exercise 1: Basic Set Operations
'''
a={1,0,12,12,222,22,True,False}
print(a)
a.add("Apoorva")
print(type(a))
a.remove("Apoorva")
print(a)
b=a.copy()
print("copied set-->",b)

#Exercise 2: Clear All Elements
a={1,4,8}
print(a)
a.clear()
print(a)



#Exercise 3: Find the Length of a Set
a={1,4,8}
print(len(a))




#Exercise 4: Check if a Set is Empty
a={21,8,764}
if len(a)==0:
    print("empty")
else:
    print("Not empty")

#Exercise 5: Union of Sets
a={"Yes","No","maybe"}
b={"Yes","No","Offcourse"}
print(a|b)

##Exercise 6: Intersection of Sets

a={"Yes","No","maybe"}
b={"Yes","No","Offcourse"}
print(a&b)

#Exercise 7: Difference of Sets
a={"Yes","No","maybe"}
b={"Yes","No","Offcourse"}
print(a-b)
print(b-a)

#Exercise 8: Symmetric Difference
a={"Yes","No","maybe"}
b={"Yes","No","Offcourse"}
print(a^b)

#Exercise 9: Find Max and Min
a={1,0,12,12,222,22}
print(max(a))
print(min(a))
'''

#Exercise 10: Sum of Set Elements
a={1,2,3,10}
sum = 0
for i in a:
    sum+= i
print(sum)