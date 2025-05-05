# Write a program to print numbers from 1 to 100 but skip multiples of 5

myvar = 0
print("Printing 1 - 100 & skipping multiple of 5")
for i in range  (100):
    i = i+1
    if i % 5 != 0 :
        print(i)
    else:
        print(f"Here is multiple of 5 -> {i}")