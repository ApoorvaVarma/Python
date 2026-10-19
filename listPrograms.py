'''#Access the third element of a list
a=[2,4,6,7,87]
print(a[2])
#********************************************************
#List Length: Print the total number of items
print("Length of list a is :",len(a))
#********************************************************
x=[]
#Check if the list is empty
if len(x)==0:
    print("list is empty")
else:
    print("list is not empty")
    '''

#********************************************************
#Change Element: Change the second element of a list to 200 and print the updated list.
'''list1=[100,500,600]
list1[1]=200
print(list1)


#Append Element: Add 600 o the end of a list and print the new list.
list2=[100,200,300]
list2.append(600)
print(list2)

#Insert Element: Insert 300 at the third position (index 2) of a list and print the result.
list3=[100,200,400]
list3.insert(2,300)
print(list3)


#Remove Element (by value): Remove 600 from the list and print the list.
list4=[100,200,400,600]
list4.remove(600)
print(list4)


#Remove Element (by index): Remove the element at index 0 from the list print the list.
list5=["hello",100,200,400,600]
list5.pop(0)
print(list5)


#Exercise 3. Sum and Average of All Numbers in a List
sum=0
list6=[2,4,6,8]
for i in list6:
    sum+=i
print(sum)
avg=sum/len(list6)
print(avg)


#Exercise 4. Find Maximum and Minimum from List
list7=[2,6,7,9]
print(max(list7))
print(min(list7))


#Exercise 5. Calculate the Product of All Elements
mult=1
list8=[2,3,10,2,1]
for i in list8:
    mult*=i
print(mult)



#Exercise 6. Count Even and Odd Numbers
list9=[2,3,10,2,1,7,9,13]
even=0
odd=0
for i in list9:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even=",even)
print("Odd=",odd)

#Exercise 7. Reverse a List
list10=[2,5,9]
list10.reverse()
print(list10)


#Exercise 8. Sort a List of Numbers
list11=[55,2,5,9]
list11.sort()
print(list11)
'''
#Exercise 9. Create a Copy of a List
list12=[55,2,5,9]
list_copy=list12
print(list_copy)
print("*****************************************")
#Exercise 10. Combine Two Lists
list13=["Hello",55,2,5,9]
list14=["World",55,2,5,9]
print(list13+list14)
