#Print first 10 numbers using a for loop
'''for i in range(1,11):
    print(i)

#Print first 10 numbers using a while loop
i=1
while i<=10:
    print(i)
    i+=1

#string ops
s="PyThon language "
print(s.replace("T","t"))
print(len(s))
print(s)

print(s*3,end=" ")

#Exercise 2. Display numbers from -10 to -1 using for loop
for i in range(-10,0):
    print(i)
print("Done")

#Calculate the sum of all numbers from 1 to N
N=int(input("enter a number: "))
sum=0
for i in range(1,N+1):
    sum+=i
print(sum)


#Exercise 6. Calculate the cube of all numbers from 1 to a given number
N=int(input("enter a number: "))
print(N**3)


#Count occurrences of a specific element in a list
l1=[2,4,6,4,20,4,8,4,4]
counter=0
for i in l1:
    if i ==4:
        counter+=1
print(counter)



#Tuple filtering 
t1 = (203,47,64,4,20,15,8,49,0.3)
filtered_tup=tuple(filter(lambda x: x<16,t1))
print(filtered_tup)


filtered_tup2=tuple(filter(lambda y: y%2==0,t1))
print(filtered_tup2)
'''

#Tuple Mapping
numbers = (1, 2, 3, 4, 5, 6)
square=tuple(map(lambda x: x**2,numbers ))
print(square)
