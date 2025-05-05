# Creating Database in Mysql

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  port="3306",
  database= "record_book"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE student_record")



print(mydb)

