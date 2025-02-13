# 2. insert the following records
 
#    100   IT
#    200   HR
#    300   Sales
#    400   Admin


import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)

try:
    mycursor = mydb.cursor()

    # Insert records into the dept table
    mycursor.execute("INSERT INTO dept (deptid, deptname) VALUES (100, 'IT')")
    mycursor.execute("INSERT INTO dept (deptid, deptname) VALUES (200, 'HR')")
    mycursor.execute("INSERT INTO dept (deptid, deptname) VALUES (300, 'Sales')")
    mycursor.execute("INSERT INTO dept (deptid, deptname) VALUES (400, 'Admin')")

    # Commit the changes to the database
    mydb.commit()

    print("Records inserted successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")
# Close the cursor and connection
mycursor.close()
mydb.close()