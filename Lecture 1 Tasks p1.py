#Basic syntax 
#Example 1

print('Hello, world')

#Python Identation
#Example 2.1

if 5>2:
    print('Five is greater than two')

#Example 2.2

a= 10
b= 20
if a<b:
    print('Var B is greater ')

#PythonComments
#This is a comment
"""
This is
a multiline 
Comment 

"""

#Pyhton Variables
#example 3.1

#Integer
rollNo = 100
#String
string = 'My name is Aizaz Khalid'
#Float
gpa = 3.2
#CHaracter
grade='A'

# Variable Casting & get the type

#casting integer into string
into_str = str(rollNo)
print('This var is ',type(into_str))

#casting int to float
into_float = float(rollNo)
print('This var is ',type(into_float))




# Multiple variables with multiple values
varOne, varTwo, varThree = 154 , "Aizaz Khalil", 3.61

#Multiple values to one variable
var_1=var_2=var_3="Pakistan"

#Unpack a Collection
Veg = ['carrot', 'Onion']
x1,x2 = Veg
print(x1)
print(x2)





