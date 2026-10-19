#WAP to print to check the number is palindrome or not
#palindrome --> 737

original_num=int(input("enter a number: "))
num=original_num
reverse =0
while num%10!=0:
    remainder=num%10
    reverse=reverse*10+remainder
    num=num//10
print(reverse)
if reverse==original_num:
    print("Palindrome")
else:
    print("Not Palindrome")





