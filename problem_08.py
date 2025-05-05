# Write a Python program to reverse a string.
# Write a program to check if a given string is a palindrome.

my_str = input("String : ")
rev_str =""

counter = len(my_str)-1
while counter>=0:
    rev_str+=my_str[counter]
    # print(my_str[counter])
    counter -= 1

print(f"Reversed string : {rev_str}")

#To check if string is a palindrome

if my_str.strip() == rev_str.strip() :
    print ("Palindrome")
else:
    print("not Palindrome")
