# 3. create table emp (empid int , empname varchar(10) , deptId int )
 
#    empid is PK
#    deptId is FK
 
#    1   A   100
#    2   B   100
#    3   C   200
#    4   D   400
#    5   E   NULL

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)

mycursor = mydb.cursor()


mycursor.execute("""
    CREATE TABLE IF NOT EXISTS emp (
        empid INT PRIMARY KEY,
        empname VARCHAR(10),
        deptId INT,
        FOREIGN KEY (deptId) REFERENCES dept(deptid)
    )
""")

# Insert the following records into emp table
mycursor.execute("INSERT INTO emp (empid, empname, deptId) VALUES (1, 'A', 100)")
mycursor.execute("INSERT INTO emp (empid, empname, deptId) VALUES (2, 'B', 100)")
mycursor.execute("INSERT INTO emp (empid, empname, deptId) VALUES (3, 'C', 200)")
mycursor.execute("INSERT INTO emp (empid, empname, deptId) VALUES (4, 'D', 400)")
mycursor.execute("INSERT INTO emp (empid, empname, deptId) VALUES (5, 'E', NULL)")

# Commit the changes to the database
mydb.commit()
print("Records inserted successfully into 'emp' table")
# Close the cursor and connection
mycursor.close()
mydb.close()