import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student_record",
    port="3306"
)

qry1 = "select * from details"
qry2 = "select name, address FROM details"
# display records in ascending order alphabetically 
sql = "SELECT * FROM details ORDER BY name"
# display records in descending order alphabetically 
sql2 = "SELECT * FROM details ORDER BY name desc"
# display records in descending order by rollno  

sql3 = "SELECT * FROM details ORDER BY rollno desc"
# Limit by 10
sql3 = "SELECT * FROM details ORDER BY rollno desc limit 10"
sql4 = "SELECT * FROM details ORDER BY rollno limit 10"
# display next 10 records
sql5 = "SELECT * FROM details ORDER BY rollno limit 10 offset 10"


mycursor = mydb.cursor()
# mycursor.execute(qry2)
# mycursor.execute(sql)
# mycursor.execute(sql2)
# mycursor.execute(sql3)
mycursor.execute(sql5)



myresult = mycursor.fetchall()
for record in myresult:

    # print("\n")
    # print(f"\t------ record ------")
    print(record)
    # print("\n")

