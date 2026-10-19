'''
a=(5,6,8,"Apoorva",True)
b=(1,)
c=5,6,8,"Apoorva",True
print(type(a))
print(type(b))
print(type(c))

#Excercise1 -creating them, retrieving individual elements using index positions, and measuring their size using len()
a=(5,6,8,False,"Apoorva",True)  #creating
print(a[3],a[4])  #retrieving with index
print("length of tuple is ", len(a))

#Exercise 2: The Trailing Comma
b=(1,)
print(b)

#Exercise 3: Tuple Repetition
c=(1,2,3)
print(c*3)

#Exercise 4: Tuple Concatenation
a=(41,2)
b=(3,4)
print(a+b)


#Exercise 5: Tuple Slicing
a=(5,6,8,"Apoorva",True,"Hi","World")
print(a[1:5])

#Exercise 6: Tuple Reversal
a=(5,6,8,"Apoorva",True,"Hi","World")
print("reversing tuple-",a[::-1])

#Exercise 7: Counting
a=(5,6,8,"Apoorva",True,"Hi","World",5)
count=0
num=5
for i in a:
    if i==num:
        count+=1
print("num comes",count,"times")        

#Exercise 8: Tuple Unpacking
a=(5,6,8)
x,y,z=a
print(x)
print(y)
print(z)
'''
#Exercise 9: The Swap Trick
a=(5,6,8)
b=(8,9,7)
a,b=b,a
print(a)
print(b)


#Exercise 10: Nested Tuple Access
'''
tp=(5,6,8,"Rishi",True,(9,7,8,"Rishi",(1,1,1.6,"Rishi",True),True))
print(tp[5][4][2])
'''