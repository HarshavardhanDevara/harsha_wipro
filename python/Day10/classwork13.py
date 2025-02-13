import mysql.connector
 
mydb = mysql.connector.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
 
mycursor = mydb.cursor()
 
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
 
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, "record(s) deleted")