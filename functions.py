'''def m(a,b):
    print("uncodemy")
    print(a+b)

m(3,5)


1. Write a Python function to find the maximum of three numbers.
2. Write a Python function to sum all the numbers in a list.
3. Write a Python function to multiply all the numbers in a list.
4. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

#WAP to define a function for sum, difference, multiplication and division
def sum(a,b):
    print("sum is", a+b)

def diff(a,b):
    print("diff is", a-b)

def mult(a,b):
    print("multiplication  is", a*b)

def div(a,b):
    print("division is", a/b)
sum(5,2)
diff(5,2)
mult(5,2)
div(5,2)


#WAP to print the even number from a range by defining functions
def printEven(num1,num2):
    for i in range(num1,num2+1):
        if i%2==0:
            print(i,end=" ")
printEven(1,13)
'''


'''
5. Write a Python program to print the even numbers from a given list.



#1. Write a Python function to find the maximum of three numbers.
def maxofThree(a,b,c):
    if a>b and a>c:
        print(a, " is the maximum of the three")
    if b>a and b>c:
        print(b, " is the maximum of the three")
    elif c>a and c>b:
        print(c, " is the maximum of the three")
maxofThree(535,77,22)


#2. Write a Python function to sum all the numbers in a list.
def sumOfList(listName):
    sum=0
    for i in listName:
        sum+=i
    print(sum)

l1=[2,4,6,8]
sumOfList(l1)

#3. Write a Python function to multiply all the numbers in a list.
def multiplyListItems(listname):
    mult=1
    for i in listname:
        mult=mult*i
    print(mult)

list2=[2,10,10]
multiplyListItems(list2)
#4. Write a Python function to calculate the factorial of a number (a non-negative integer). 
# The function accepts the number as an argument.
def fact(x):
    factorial_x=1
    for i in range(1,x+1):
        factorial_x=factorial_x*i
    print(factorial_x)
fact(4)

'''
#5. Write a Python program to print the even numbers from a given list.
def printEvenofList(listname):
    for i in listname:
        if i%2==0:
            print(i,end=" ")
l3=[2,3,4,5,6,7,8,9,10,11]
printEvenofList(l3)