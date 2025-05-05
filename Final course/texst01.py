import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_record",
    port=3306
)

print("Connection successful:", mydb.is_connected())


