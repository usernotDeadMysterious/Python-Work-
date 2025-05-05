file = open ("Data.txt",'r')
search =  input("Enter Name or Roll no. of student to search for Record : ")
search = search.upper()
flag = True

for record in file:
    if search in record:
        std_data= record

        print(std_data.replace(",","\n"))
        flag = False

if flag == True:

    print("\n\t404 Error \n")
    print("\tRecord of the student not Found \n")

file.close()
