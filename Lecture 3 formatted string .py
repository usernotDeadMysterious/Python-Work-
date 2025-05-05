name = input("Enter your full name: ")
# name = "Aizaz Khalid"
rollno = int (input("Enter your Roll no: "))
# rollno = 154
cnic =int(input("Enter your CNIC without dashes: ") )

# cnic = 1730172626849
gpa = float(input('Enter your gpa: '))
# gpa = 3.61

studentData=[name,rollno,cnic,gpa]
# name = studentData[0]
# rollno = studentData[1]
# cnic = studentData[2]
# gpa = studentData[3]

# qry = f'''
# Name of candidate: {name}
# Roll no. of candidate: {rollno}
# CNIC of candidate: {cnic}
# Gpa of candidate: {gpa}
# '''

# print (qry)

print(studentData)

writeFile = open ("abc.txt","a")
writeFile.write (str(studentData))
writeFile.close()

# studentData = open ("abc.txt","a")