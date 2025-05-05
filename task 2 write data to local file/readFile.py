
file = open('studentData.txt', 'r')
# Get the search term from the user
search_term = input("Search the Record of Student by one of the following : Full Name: CNIC: Roll no: or GPA:\n")

found = False
    # Read the file line by line
for record in file:
        # Check if the search term is in the record
    if search_term in record:
        print("Record found\n" + record.strip())  
        # Print the found record
        found=True
        # Stop searching after finding the record
        break  
if found == False:
    print("Record of the student does'nt exist ")
# Close the file
file.close()

