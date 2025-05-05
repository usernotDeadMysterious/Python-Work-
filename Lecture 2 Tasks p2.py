#python Numbers
#int
x = 1
#float
y = 3.1
#complex
z = 5j

print(type(x))
print(type(y))
print(type(z))



#Strings
#single quotes
print('Hello Pakistan')
#double Quotes
print("Hello Pakistan")
#Multi line strings

my_Str = """

To,
Director NCCS
UET, Peshawar.

Subject: Application for Leave

I am not feeling well today kindly grant me a leave 
I shall be very thankfull

your sincerely,
XYZ

"""

print(my_Str)

#Strings As Arrays
my_Str2 = 'Pakistan'

print(my_Str2[0])
print(my_Str2[1])
print(my_Str2[2])

#Length Function  len()

print(len(my_Str2))

#check certain characters/string in strings

print('Pak' in my_Str2)

if 'Pak' in my_Str2:
    print('Yes The string is present')
else:
    print('String is not present')


#Slicing 

print(my_Str2[0:3])
print(my_Str2[0:])
print(my_Str2[:3])
print(my_Str2[:-1])
print(my_Str2[-5:-2])


#String Functions

new_Str = "              University of Agriculture, peshawar           "
print("Upper Func",new_Str.upper())
print("Strip Func",new_Str.strip())
print("Lower Func",new_Str.lower())
print("Split Func",new_Str.split(","))
print("Replace Func",new_Str.replace("peshawar","Pakistan"))


