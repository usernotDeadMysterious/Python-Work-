# Write a program to calculate the sum of all even numbers between 1 and 50.
even_Sum=0
for i in range(50):
    i = i+1
    
    if i % 2 == 0 :
        even_Sum += i
        
print("sum of all even numbers between 1 and 50 : ",even_Sum)