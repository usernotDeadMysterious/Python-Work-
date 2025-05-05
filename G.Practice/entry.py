import os
file_name = "mydata.txt"
if os.path.exists(file_name):
    file=open("mydata.txt","a")
else:
    file=open("mydata.txt","x")
file.close()