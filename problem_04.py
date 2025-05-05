# Write a Python program to print the multiplication table of a given number.

number = int (input("ENTER NUMBER : "))

for i in range(10):
    ttl=number*(i+1)
    print(f"{number} * {i+1} = {ttl}")