# Declared a counter variable for Data Entry of No. of Students As user wants

counter = int(input("How many students data you want to Enter to the database : "))

#opening a file to write the data of students
file = open('Data.txt','a')

#for calculating percentage
totalmarks = 500

#initiating a loop for no. of students data Entry
for i in range(counter):

    name = input("Enter Name of the student : ")
    roll_no = input("Enter Roll no. of the student : ")
    mpl = input("Enter marks in Modern Programming Language Subject : ")
    psycology = input("Enter marks in Psycology Subject : ")
    dpcomputing = input("Enter marks in Distriuted & Parallel Computing Subject : ")
    dip = input("Enter marks in Digital Image Processing Subject : ")
    fyp1 = input("Enter Marks in Final year project 1 : ")
    

    obtainedmarks = int(mpl)+int(psycology)+int(dpcomputing)+int(dip)+ int (fyp1)

    #calcuating %age
    percentage = float(obtainedmarks/totalmarks)*100

    record = f"Name : {name.upper()} , Roll no. : {roll_no} , Python : {mpl} , Psycology : {psycology} , Distriuted & Parallel Computing : {dpcomputing} , Digital Image Processing : {dip} , Final year Project 1 : {fyp1} , Obtained Marks : {obtainedmarks} , Total Marks : {totalmarks} , Percentage : {percentage} \n"
    
    file.write(record)

    print(f"Data of {name} entered to the Database Successfully")

file.close()
if counter == 1:
    print(f"Data Entry of {counter} Student Completed ")
else:
    print(f"Data Entry of {counter} Students Completed ")





