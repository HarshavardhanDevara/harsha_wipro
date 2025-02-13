# Q3   List empname who does work under any deparments
# write python script to connnect mysql and do the task given above

import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT empname FROM emp WHERE deptId IS NULL")
result = mycursor.fetchall()
print("Employees who do not work under any department:")
for row in result:
    print(row[0])

# Close the cursor and connection
mycursor.close()
mydb.close()