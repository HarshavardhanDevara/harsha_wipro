import MySQLdb

# Connect to the database
mydb = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
mycursor = mydb.cursor()

# Corrected SQL UPDATE statement
mycursor.execute("UPDATE customers SET name='harsha', address='tpt' WHERE name='john'")

# Commit the changes to the database
mydb.commit()

# Fetch and print the updated records
mycursor.execute("SELECT * FROM customers WHERE name='harsha' AND address='tpt'")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)

# Close the cursor and connection
mycursor.close()
mydb.close()