# 1. Create table dept with deptid and deptname . deptiId is Pm Key
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

try:
    # Create table if it does not exist
    mycursor.execute("""
        CREATE TABLE IF NOT EXISTS dept (
            deptid INT PRIMARY KEY,
            deptname VARCHAR(50)
        )
    """)
    print("Table 'dept' created successfully")
except mysql.connector.Error as err:
    print(f"Error: {err}")

# Close the cursor and connection
mycursor.close()
mydb.close()