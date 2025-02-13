# Q1 . list all emp who works in some dept
import mysql.connector

# Connect to the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)

mycursor = mydb.cursor()


mycursor.execute("SELECT empname FROM emp WHERE deptId IS NOT NULL")
result = mycursor.fetchall()
print("Employees who work in some department:")
for row in result:
    print(row[0])

# Close the cursor and connection
mycursor.close()
mydb.close()