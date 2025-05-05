# Write a Python program to swap two variables.

myvar1 = 30
myvar2 = 50
print(f"Before Swapping \nvariable 1 = {myvar1}\nvariable 2 = {myvar2}")
temp = 0
temp = myvar1
myvar1 = myvar2
myvar2 = temp
print("After Swapping")
print(f"variable 1 = {myvar1}\nvariable 2 = {myvar2}")
