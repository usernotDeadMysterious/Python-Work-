
counter =int(input("How many Records do you want to enter (e.g : 1,2,3....): "))
for x in range (counter):
    name = input("Enter your full name: ")
    # name = "Aizaz Khalid"
    rollno = int (input("Enter your Roll no: "))
    # rollno = 154
    cnic =int(input("Enter your CNIC without dashes: ") )
    # cnic = 1730172626849
    gpa = float(input('Enter your gpa: '))
    # gpa = 3.61
    writeFile = open ("studentData.txt","a")
    writeFile.write(f"Name: {name} , Rollno : {rollno} , CNIC: {cnic} , GPA: {gpa}\n")
    writeFile.close()
    # writeFile.write(str([name,rollno,cnic,gpa]))
    # writeFile.write("\n")
    print("Data written to the file successfully")
