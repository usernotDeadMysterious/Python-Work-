# Write a Python program to find the largest of three numbers.

var1=int(input("Enter 1st Number : "))
var2=int(input("Enter 2nd Number : "))
var3=int(input("Enter 3rd Number : "))

if var1 > var2 and var1>var3:
    print(f"{var1} is Greater than {var2} & {var3}")
elif var2 > var1 and var2>var3:
    print(f"{var2} is Greater than {var1} & {var3}")
else:
    print(f"{var3} is Greater than {var1} & {var2}")