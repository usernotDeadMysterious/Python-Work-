file = open("studentData.txt","r")

for record in file:
    print(record)

file.close()