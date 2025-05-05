# Insert command in Mysql

import mysql.connector
# mydb = 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="student_record",
  port="3306"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE details (name VARCHAR(255), address VARCHAR(255), rollno int(5))")

# mycursor.execute("SHOW TABLES")
# qry1 = 'INSERT into student_record (name, address, rollno) VALUES ("John Smith","123 Elm Street",1)'
sql = "INSERT INTO details (name, address, rollno) VALUES (%s, %s, %s)"

val = [
    ('John Smith','123 Elm Street',1),
    ('Sarah Johnson','456 Oak Avenue',2),
    ('Michael Brown','789 Pine Road',3)
    
]
val2 = [
    ('Emily Davis', '101 Maple Drive', 4),
    ('Daniel Wilson', '202 Cedar Lane', 5),
    ('Laura Martinez', '303 Birch Court', 6),
    ('Kevin Garcia', '404 Walnut Street', 7),
    ('Angela Moore', '505 Aspen Way', 8),
    ('Jacob Taylor', '606 Chestnut Circle', 9),
    ('Sophia Anderson', '707 Spruce Boulevard', 10),
    ('Ryan Thomas', '808 Hickory Place', 11),
    ('Chloe White', '909 Magnolia Crescent', 12),
    ('Brandon Harris', '1001 Willow Terrace', 13),
    ('Olivia Clark', '1102 Fir Street', 14),
    ('Ethan Lewis', '1203 Redwood Parkway', 15),
    ('Mia Walker', '1304 Cypress Close', 16),
    ('Liam Young', '1405 Poplar Avenue', 17),
    ('Isabella Hall', '1506 Alder Alley', 18),
    ('Noah Wright', '1607 Sycamore Drive', 19),
    ('Ava King', '1708 Juniper Grove', 20),
    ('Emma Hernandez', '1809 Cedarwood Lane', 21),
    ('James Martinez', '1901 Aspen Ridge', 22),
    ('Grace Wilson', '2002 Maplewood Drive', 23),
    ('Benjamin Lee', '2103 Oakfield Avenue', 24),
    ('Ella Turner', '2204 Willowbend Court', 25),
    ('Lucas Walker', '2305 Pineview Lane', 26),
    ('Amelia Adams', '2406 Sprucehill Way', 27),
    ('Henry Lopez', '2507 Chestnut Glen', 28),
    ('Zoe Carter', '2608 Birchwood Path', 29),
    ('Mason Reed', '2709 Redwood Trail', 30),
    ('Harper Parker', '2801 Walnut Cove', 31),
    ('Elijah Rivera', '2902 Magnolia Park', 32),
    ('Scarlett Ross', '3003 Juniper Meadow', 33),
    ('Jack Scott', '3104 Sycamore Lane', 34),
    ('Lily Cooper', '3205 Alderwood Drive', 35),
    ('Oliver Sanchez', '3306 Poplar Terrace', 36),
    ('Aria Peterson', '3407 Cedar Ridge', 37),
    ('Logan Howard', '3508 Aspen Point', 38),
    ('Charlotte Jenkins', '3609 Willow Ridge', 39),
    ('William Ward', '3701 Oakwood Drive', 40),
    ('Abigail Murphy', '3802 Pinefield Path', 41),
    ('Alexander Bailey', '3903 Maple Crest', 42),
    ('Sofia Foster', '4004 Birch View', 43),
    ('Aiden Morgan', '4105 Redwood Hill', 44),
    ('Hannah Fisher', '4206 Spruce Bend', 45),
    ('Matthew Edwards', '4307 Chestnut Valley', 46),
    ('Victoria Bell', '4408 Walnut Ridge', 47),
    ('Joshua Bennett', '4509 Cedarwood Glen', 48),
    ('Ella Clark', '4601 Poplar Lane', 49),
    ('Liam Collins', '4702 Alder Meadow', 50)
]
# mycursor.executemany(sql,val)
# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# mycursor.execute("SELECT * from student_record")


# for x in mycursor:
#   print(x)
try:
    mycursor.executemany(sql, val2)
    mydb.commit()
    print(mycursor.rowcount, "records were inserted.")
except mysql.connector.Error as err:
    print("Error: ", err)