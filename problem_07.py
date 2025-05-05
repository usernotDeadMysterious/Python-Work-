# Write a program to count the number of vowels in a given string.

# a = "Aizaz Khalid"
a = input("Enter a string to count vowels in string : ")
# strings are arrays
vowels=0
for i in a.lower():
    # print(i)
    if i == "a" or i=="e" or i=="i" or i=="o" or i=="u":
        vowels+=1
    
print("vowels = "+ str(vowels))