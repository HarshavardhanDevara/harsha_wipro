# Q2   list deptname who does not have employee
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
    SELECT deptname FROM dept 
    WHERE deptid NOT IN (SELECT deptId FROM emp WHERE deptId IS NOT NULL)
""")
result = mycursor.fetchall()
print("Departments without employees:")
for row in result:
    print(row[0])

# Close the cursor and connection
mycursor.close()
mydb.close()