import mysql.connector
 
mydb = mysql.connector.connect(                    
    host="localhost",
    user="root",
    passwd="Harsha@1807#",
    db="rps"
)
mycursor = mydb.cursor()
 
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
 
mycursor.execute(sql)
 
mydb.commit()
 
print(mycursor.rowcount, "record(s) affected")
 